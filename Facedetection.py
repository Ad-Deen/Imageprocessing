import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('Sample images and videos\crowd 2.jpg')
# # print(img.shape)
# #cv.imshow('nature',img)
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('crowd', grey)
haar = cv.CascadeClassifier('haar_face_detector.xml')

# facedetect = haar.detectMultiScale(grey,scaleFactor = 1.1 , minNeighbors = 1)
# print(len(facedetect))

#rectangling the faces that are detected
# for x,y,i,j in facedetect:
#     (cv.rectangle(img,(x,y),(x+i,y+j),(0,255,0),3))
# cv.imshow('marked faces',img)
# cv.waitKey(0)

#rectangling the faces in video
# for x,y,i,j in facedetect:
#     (cv.rectangle(frame,(x,y),(x+i,y+j),(0,255,0),3))
# cv.imshow('marked faces',img)
# cv.waitKey(0)


capture = cv.VideoCapture(0)
while True:
    isTrue , frame = capture.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #cv.imshow('crowd', grey)
    facedetect = haar.detectMultiScale(grey,scaleFactor = 1.1 , minNeighbors = 1)
    for x,y,i,j in facedetect:
        (cv.rectangle(frame,(x,y),(x+i,y+j),(0,255,0),3))
     
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
capture.release() 
cv.destroyAllWindows() 