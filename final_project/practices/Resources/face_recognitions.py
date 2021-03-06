import cv2 as cv
import numpy as np

# instance the face detecting classifier
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#load the features and labels
""" features = np.load('features.npy')
labels = np.load('labels.npy') """

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Faces/val/ben_afflek/1.jpg')
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)

#detect face in the picture
face_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face_rect:
    faces_roi=gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label={people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w, y+h),(0,255,0),thickness=2)

cv.imshow('Detected face',img)

cv.waitKey(0)