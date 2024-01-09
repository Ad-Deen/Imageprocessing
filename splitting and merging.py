import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)
blank = np.zeros(img.shape[:2],dtype='uint8')

#splitting the image based on color components and watching in gray scale
b,g,r = cv.split(img)
# cv.imshow('blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

#merging back the split color
cv.imshow('merged',cv.merge([b,g,r]))

#way to see split colors out of grey scale
cv.imshow('blue',cv.merge([b,blank,blank]))
cv.imshow('Green',cv.merge([blank,g,blank]))
cv.imshow('Red',cv.merge([blank,blank,r]))

cv.waitKey(0)