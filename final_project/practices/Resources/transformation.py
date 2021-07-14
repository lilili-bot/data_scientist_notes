import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')

cv.imshow('Lady', img)

# translation, shift image from x to y axis, rotation, resizing
def translate(img, x, y): 
    '''
    x and y stands for the picso, need to be translated along x, and y
    '''
    transMat = np.float32([[1,0,x],[0,1,y]])# this is a translation matrix
    dimensions = (img.shape[1], img.shape[0]) # shape 1 is the width, shape 0 is the higth

    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 200, -100)

cv.imshow('Translated Image', translated)

# -x, to the left, -y shifting it to  up, x right, y down.
 
#rotation
def rotate(img, angle, rotPoint=None):

    (height, width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated',rotated)
# resizing
resized=cv.resize(img,(100,500), interpolation=cv.INTER_CUBIC)

cv.imshow('resized',resized)

# flipping image

flip = cv.flip(img, -1)
cv.imshow('flip-1', flip)

# cropping
cropped = img[200:400, 100:300]
cv.imshow('cropped', cropped)

cv.waitKey(0)