import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('greyscale',grey)


# #Using histogramss on mask
# blank = np.zeros(img.shape[:2],dtype = 'uint8')
# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# #cv.imshow('mask',mask)
# masked = cv.bitwise_and(grey,grey,mask = mask)
# cv.imshow('high',masked)

# #greyscale histograms
# grey_hist= cv.calcHist([grey],[0],masked,[256,],[0,256])

# #plotting the histogram
# plt.figure()
# plt.title('grey scale pixel intensity')
# plt.xlabel('Bins')
# plt.ylabel('No. of pixels')
# plt.plot(grey_hist)
# plt.xlim([0,256])
# # plt.ylim([0,8000])
# plt.show()

#histograms of color images
plt.figure()
plt.title('grey scale pixel intensity')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b','g','r')
for i , col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
   

plt.show()

cv.waitKey(0)