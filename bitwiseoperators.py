import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
#cv.imshow('nature',img)

blank = np.zeros((800,800),dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(),(100,100),(700,700),255,-1)
circle = cv.circle(blank.copy(),(400,400),400,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise AND >> intersecting regions
# cv.imshow('And ', cv.bitwise_and(rectangle,circle))

# #bitwise OR >> intersecting + non intersecting
# cv.imshow('OR', cv.bitwise_or(rectangle,circle))

# #XOR >> non intersecting
cv.imshow('XOR',cv.bitwise_xor(rectangle,circle))

#bitwise NOT
XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('NOT', cv.bitwise_not(XOR))

cv.waitKey(0)