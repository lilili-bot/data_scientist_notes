import cv2 as cv
import numpy as np

'''
this file is about how to split and merge image spaces and channels. 
eg. RGB are based on red, gree, and blue, how to get the components.
'''
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank,g, blank])
red = cv.merge([blank, blank,r])



cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

cv.imshow('Blue_blank',blue)
cv.imshow('Green_blank',green)
cv.imshow('Red_blank',red)
# brighter shows that more picsos in the area with respect of the color channel.
print(img.shape)
print(b.shape) # they have the shape of 1
print(g.shape)
print(r.shape)

# merge the chanles together

merged = cv.merge([b,g,r])
cv.imshow('Merged bgr', merged)

cv.waitKey(0)