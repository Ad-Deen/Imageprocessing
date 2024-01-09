import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)

#Changing color to hsv
cv.imshow('hsv', cv.cvtColor(img,cv.COLOR_BGR2HSV))

#changing to lab
cv.imshow('lab', cv.cvtColor(img,cv.COLOR_BGR2LAB))

#changing to gray
cv.imshow('grey', cv.cvtColor(img,cv.COLOR_BGRA2GRAY))

#changing to RGB from BGR to interact with other py libs like matplotlib
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.show()

cv.waitKey(0)