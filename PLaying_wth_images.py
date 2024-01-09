import cv2 as cv
import numpy as py

img = cv.imread('Sample images and videos\L1.jpg')
cv.imshow('lion',img)


# Convertion to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grey',gray)
# cv.waitKey(0)
# blur
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# cv.waitKey(3000)
# Finding edge in image
# Canny = cv.Canny(img,100,20)
# cv.imshow('Canny',Canny)
# cv.waitKey(3000)
# Dilating the image
# dilimg = cv.dilate(Canny,(3,3),iterations=1)
# cv.imshow('dilimg',dilimg)
# cv.waitKey(3000)
# eroding image
# eroded = cv.erode(dilimg,(3,3),iterations=1)
# cv.imshow('eroded',eroded)
# cv.waitKey(0)
# resizing image
# resized = cv.resize(img,(1000,1000),interpolation=cv.INTER_CUBIC) #higher scale inter area or cubic
# cv.imshow('resized',resized)            #lower scale inter linear

#Cropping
cropped = img[20:100,20:40]
cv.imshow('cropped',cropped)
cv.waitKey(0)