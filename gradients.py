import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('greyscale',grey)
# #gradients and edge detection is mathmatically different
# #other ways to find edges
# #leplacion method
# lap = cv.Laplacian(grey,cv.CV_32F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('laplacion',lap)

#using sobel method that divides the image into x and y axis parts and combine with or operator to get combined picture
sobelx = cv.Sobel(grey,cv.CV_64F,1,0)
sobely = cv.Sobel(grey,cv.CV_64F,0,1)
combined = cv.bitwise_or(sobelx,sobely)
cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('sobel combined', combined)

canny = cv.Canny(grey,125,150,)
cv.imshow('canny',canny)


cv.waitKey(0)