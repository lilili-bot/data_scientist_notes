import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

# thresholded img is binary, first set gray.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# Simple Thresholding
threshold, binary_img = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Binary_img',binary_img)


threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Binary_img_inv',thresh_inv)

#Adaptive thresholding, 

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive_thresholding', adaptive_thresh)






cv.waitKey(0)