import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8') # the blank image need to be the same as the original img.
cv.imshow('Blank Image',blank)

mask = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Maksed_circle', masked)

mask_rectangle = cv.rectangle(blank,(0,0),(img.shape[1]//2, img.shape[0]//2),255,-1)
masked_rectangle = cv.bitwise_and(img,img,mask=mask_rectangle)
cv.imshow('Masked_rectangle',masked_rectangle)


gray_hist = cv.calcHist(
    [masked_rectangle], # a list of images
    [0], # the number of the channel
    mask_rectangle, #provide a mask
    [256], # the number of the bins
    [0,256] #the range of all possible picso values
)
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

colors=('b','g','r')
for i, col in enumerate(colors):
    print(i, col)



cv.waitKey(0)