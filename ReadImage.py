import cv2 as cv

from Resize_rescale import rescaleFrame

#img = cv.imread('Sample images and videos\L1.jpg')
#cv.imshow('Lion', img)
#cv.waitKey(0)

capture = cv.VideoCapture('Sample images and videos\production ID-4524598.mp4')
while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', rescaleFrame(frame, scalewidth=1, scalehight=.4) )
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
capture.release() 
cv.destroyAllWindows()  