import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)

#averaging
avg = cv.blur(img ,(3,3))
cv.imshow('Avg blur',avg)

#Gaussian blurr
cv.imshow('Gaussian blurr', cv.GaussianBlur(img,(3,3), 0 ))

#Median blurr (more affective in reducing noise)
cv.imshow('Median blurr', cv.medianBlur(img,3,))

#Bilateral blurrring(blurres the image but edges remain clear)
cv.imshow('bilateral', cv.bilateralFilter(img,100,15,15) )

cv.waitKey(0)