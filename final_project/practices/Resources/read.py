import cv2 as cv

#img = cv.imread('Photos/cat_large.jpg')
#cv.imshow('Cat',img)

capture = cv.VideoCapture('Videos/dog.mp4')
#0 is the webcam 1 is the first camrea attached to the mac.
# reading videos is different from reading image. Video is made of all frames, so we are reading all frames and imshow all frames.


#error -225 meaning can not find the image or video. happens when the video is finished. 

# reshaping/ rescaling  the video
# downscale to smaller value. 20p, 100p or higher is not supported by the camera.



#cv.waitKey(0)

while True:
    isTrue, frame = capture.read()


    cv.imshow('Videos', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # press d, and stop imshow the video
      break

capture.release()
cv.destroyAllWindows() 