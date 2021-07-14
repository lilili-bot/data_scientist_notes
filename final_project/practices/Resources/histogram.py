import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
get the picso distribution in a images
'''

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale histogram
gray_hist = cv.calcHist(
    [gray], # a list of images
    [0], # the number of the channel
    None, #provide a mask
    [256], # the number of the bins
    [0,256] #the range of all possible picso values
)

""" plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show() """

# compute a color histogram
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked image', masked)
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i],circle,[256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim=([0,256])
plt.show()






cv.waitKey(0)