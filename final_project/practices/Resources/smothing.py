import cv2 as cv
import os

path = '/Users/lilycheng/Desktop/dash/assets'
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)
cv.imwrite(os.path.join(path , 'Cats.jpg'), img)
# average blur
average = cv.blur(img, (7,7)) # using 8 numbers' average as the value of the middle
cv.imshow('Average blur', average)
cv.imwrite(os.path.join(path , 'Average blur.jpg'), average)
#gauss blur
gauss = cv.GaussianBlur(img, (7,7),0) # gives each of number a weight, so the middle cell is a weigthed average.
cv.imshow('Gaussian blur', gauss)
cv.imwrite(os.path.join(path , 'Gaussian blur.jpg'), gauss)
# median blur -> more effective in smothing. size bigger than 5 is not effective for median blur.
median = cv.medianBlur(img,5) # the kernal size is not a touple, but a interger. 
cv.imshow('median blur', median)
cv.imwrite(os.path.join(path , 'median blur.jpg'), median)

#bilateral , advandages it blur but keep the edges
bilateral = cv.bilateralFilter(gauss,5,15,15)
cv.imshow('bilateral', bilateral)
cv.imwrite(os.path.join(path , 'bilateral_gauss.jpg'), bilateral)


cv.waitKey(0)