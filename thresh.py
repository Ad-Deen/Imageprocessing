import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)

#Thresholding simple
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thresholdinp , thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
cv.imshow('avg threshhold', thresh)
#inverse threshold

thresholdinp , thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
#cv.imshow('avg threshhold inv', thresh)

#adaptive threshholding
adaptive_thresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,2)
cv.imshow('adaptive',adaptive_thresh)

cv.waitKey(0)