import cv2 as cv

img = cv.imread('Photos/Cat.jpg')

# convert BGR image into gray scale
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_img',gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (3,3) is the kernal size, more blur, bigger kernal
cv.imshow('Blured img', blur)


#Edge Cascode

canny = cv.Canny(blur, 125, 175)

cv.imshow('Canny',canny)

# dialating the image

dilated = cv.dilate(canny,(7,7), iterations=3)

cv.imshow('Dilated image', dilated)

# Eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded dilated', eroded)

# resize
resized = cv.resize(img, (250,250), interpolation=cv.INTER_CUBIC) # CUBIC is slow but good quality of image, area and linear is faster but lower quality.
cv.imshow('Resized Cat', resized)

# Cropping 
cropped = resized[50:200,200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)