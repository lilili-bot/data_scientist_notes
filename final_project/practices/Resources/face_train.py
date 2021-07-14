import cv2 as cv
import os
import numpy as np


people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# one way to create the list of the label.

""" p = []

for i in os.listdir(r'Faces/train'):
    p.append(i)
print(p) """

DIR = r'Faces/train'

# or write a function to get the training data

features=[]
labels=[]

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in face_rect:

                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
    return features, labels
create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}') 

features = np.array(features,dtype='object')
labels=np.array(labels)
# now we have already the list of features and labels, we can start training them model.
# instance the model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train
face_recognizer.train(features, labels)

# saving model
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

print('Training is done ---------------')