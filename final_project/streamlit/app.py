import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

def detect_objects(my_image):

    st.set_option('deprecation.showPyplotGlobalUse', False)
    col1, col2 = st.beta_columns(2)

    col1.subheader("Original Image")
    st.text("")
    plt.figure(figsize=(15,15))
    plt.imshow(my_image)
    col1.pyplot(use_column_width=True)
    
   
    #plt.imshow(my_image)
    

    #print ('Upload Yolo Algorithm')

    net = cv2.dnn.readNetFromDarknet('models/yolov4-obj.cfg','models/yolov4-obj_best.weights')
    classes = []
    with open('models/obj.names','r')as f:
        classes = [line.strip() for line in f.readlines()]
    #print(classes)

    new_img = np.array(my_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)

    ht, wt = img.shape[:2]
    
    blob = cv2.dnn.blobFromImage(new_img,1/255,(416,416),(0,0,0),swapRB=True,crop = False)
    
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    #print(layer_out[0].shape)


    boxes = []
    confidences = []
    class_ids = []

    outs = net.forward(output_layers)

    for output in outs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > .6:
                center_x = int(detection[0]*wt)
                center_y = int(detection[1]*ht)
                w = int(detection[2]*wt)
                h = int(detection[3]*ht)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
    #indexes = cv2.dnn.NMSBoxes(boxes, confidences,.5,.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size=(len(boxes),3))

    score_threshold = st.sidebar.slider("Confidence Threshold", 0.00,1.00,0.5,0.01)
    nms_threshold = st.sidebar.slider("NMS Threshold", 0.00, 1.00, 0.4, 0.01)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences,score_threshold,nms_threshold) 

    items = []

    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i],2))
        color = colors[i]
        cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
        cv2.putText(img, label+""+confidence,(x,y+20),font,2,(0,0,0),2)
        items.append(label)
    
    st.text("")
    col2.subheader("Object Detection Result")
    st.text("")
    plt.figure(figsize = (15,15))
    plt.imshow(img)
    col2.pyplot(use_column_width=True)

    if len(indexes)>1:
        st.success("Found {} Objects - {}".format(len(indexes),[item for item in set(items)]))
    else:
        st.success("Found {} Object - {}".format(len(indexes),[item for item in set(items)]))
    

def object_main():
    """OBJECT DETECTION APP"""

    gif_runner = st.image('GIF/home_office.gif')
    

    st.title("Home,My Sweet Home Demo")
    st.subheader("Spiced Academy Data Science BootCamp- Jalapenalty Final Project")
    st.write("Lili Cheng")
    st.write('''The algorithm implemented below is retrained YOLOV4. 
    It has 2 Classes, they person and cat. As the first pharse of a plan to implement a smart light system at home.''')

    choice = st.radio("", ("Show Demo", "Browse an Image"))
    st.write()

    if choice == "Browse an Image":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

        if image_file is not None:
            my_image = Image.open(image_file)  
            detect_objects(my_image)

    elif choice == "Show Demo":
        my_image = Image.open("images/cats.jpg")
        detect_objects(my_image)
    
    with st.beta_expander("Video Results Yolov4 v.s Yolov4 Re-Trained"):

       col1, col2 = st.beta_columns(2)
       with col1.subheader("Yolov4"):
           video_file1=open('videos/walking_up_results.mp4','rb')
           video_bytes = video_file1.read()
           st.video(video_bytes,start_time=0)
       with col2.subheader('Yolov4 Retrained 2 Classes'):
           video_file2=open('videos/walking_up_90_best_2classes.mp4','rb')
           video_bytes = video_file2.read()
           st.video(video_bytes,start_time=0)
    
    st.write('11-June-2021')
    st.write('Stuttgart')

       







if __name__ == '__main__': 
    #my_image = cv2.imread('images/Cats.jpg')
    #detect_objects(my_image)
    object_main()
    