import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
plt.imshow(img)
plt.show()

'''this file is about how to switch color spaces of the images among bgr, gbr, lab, hsv
opencv is by default taking bgr images
'''

# BGR to Gray scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
#plt.imshow(rgb)
#plt.show()

'''we can convert hsv, gray lab to BGR '''

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr', lab_bgr)

# for gray to lgb needs 2 step, first gray -> bgr -> lab



cv.waitKey(0)