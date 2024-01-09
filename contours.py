#Basically the boundaries of objects
import cv2 as cv
import numpy as np


img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)

#Creating a blank page
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)
#grayscaling the image to have more visible edges
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('grey',gray)

#Using canny to figure out the edges
canny = cv.Canny(gray,125,150,)
cv.imshow('canny',canny)

#thresholding the image to figure out edges (Canny alternate)
ret , thresh = cv.threshold(gray,125,150,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)


#using contours gives out a python list of all the co ordinates of the image pixels
contours , hierarchy = cv.findContours(thresh , cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

#writing the contour lines on the blank page
cv.drawContours(blank,contours,-1,(255,255,255),1)
cv.imshow('cont drawn',blank)
print(hierarchy)

cv.waitKey(0)