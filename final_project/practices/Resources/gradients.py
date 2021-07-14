import cv2 as cv
import numpy as np
import os

path = '/Users/lilycheng/Desktop/dash/assets'
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.imwrite(os.path.join(path , 'gray_cat.jpg'), gray)
# laplacian edages
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
cv.imwrite(os.path.join(path , 'laplacian.jpg'), lap)
#sobel
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imwrite(os.path.join(path , 'sobelx.jpg'), sobelx)
cv.imwrite(os.path.join(path , 'sobely.jpg'), sobely)
#combine sobel
combined_sobelxy = cv.bitwise_or(sobelx,sobely)
cv.imshow('combined_sobel',combined_sobelxy)
cv.imwrite(os.path.join(path , 'combined_sobelxy.jpg'), combined_sobelxy)

#canny
canny = cv.Canny(gray,150,175) #?? what is the meaning of the threshold here
cv.imshow('canny',canny)
cv.imwrite(os.path.join(path , 'canny.jpg'), canny)


cv.waitKey(0)