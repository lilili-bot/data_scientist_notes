import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)
# create a blank for drawing the all the contours.
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#step 1 is to convert RGB img to gray image
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Gray',gray)

#step2 is to find the cannys
canny = cv.Canny(img, 125,175) # canny is a edge detector
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

# the shape contours are 2703, which is a lot, try to blur the image first.break
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny_blur = cv.Canny(blur, 125,175) # canny is a edge detector
cv.imshow('Canny Edges', canny_blur)
contours_blur, hierarchies_blur = cv.findContours(canny_blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours_blur))

# instead of bluring the image, cv.threshhold is turning the image to binary image, which is white and black
ret, thresh_gray = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh_gray)
contours_thresh, hierarchies_thresh = cv.findContours(thresh_gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours_thresh))

cv.drawContours(blank, contours_blur, -1,(0,0,255),2)
cv.imshow('Drawn contours',blank)

# conclusion, better blur then canny and find the contours. Other than using threshold.



cv.waitKey(0)