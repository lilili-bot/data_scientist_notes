import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank', blank)


# 1. paint the image a certain color

# blank[:] = 0,255,0 # full screen
blank[200:300, 300:400] = 0,0,223 # blank is 500*500 picsos.

#cv.imshow('Green', blank)

# 2. drae a rectangle
#windowname = 'Retangle'
#start_point = (0,0)
#end_point = (250,250)
#color = (255,0,0)
#thickness = 2
#cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED)
#another way to get the start point and end point

cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)


# draw a circle

cv.circle(blank,(250,250),40,(0,0,255),thickness=cv.FILLED) # radio of 40 picsos

# draw a line

cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness=2)

#write a text on a image

cv.putText(blank,'my first text',(blank.shape[0]//2,blank.shape[1]//2), cv.FONT_HERSHEY_SCRIPT_SIMPLEX,1.0,(255,255,255),2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
