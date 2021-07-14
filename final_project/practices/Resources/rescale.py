import cv2 as cv

# reading videos
capture = cv.VideoCapture('Videos/dog.mp4')
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
def rescaleFrame(frame, scale = 0.20):
# this is for img, videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('resized_image', resized_image)

def changeRes(width, height):
    # this is only for changing Res for live video
    capture.set(3, width)
    capture.set(4,height)
    pass

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Videos', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): # press d, and stop imshow the video
      break

capture.release()
cv.destroyAllWindows() 