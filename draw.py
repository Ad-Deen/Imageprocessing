import cv2 as cv
import numpy as np
blank  = np.zeros((700,1000,3), dtype='uint8')
cv.imshow('blank', blank )
#painting the canvas with monocolor
blank[:] = 0,255,0
cv.imshow('green',blank )
i= 0
j = 150
k = 220
blank[:] = i,j,k
cv.imshow('green1',blank )
cv.waitKey(0)
#rectangle
cv.rectangle(blank,(0,0),(350,500),(0,150,150),thickness=6) 
cv.imshow('rectangle',blank)
# cv.waitKey(0)
# #circle
cv.circle(blank,(300,300),50,(150,200,41),-1)
cv.imshow('circle',blank)
# cv.waitKey(0)
# #line
cv.line(blank,(300,300),(500,300),(150,200,41),6)
cv.imshow('circle',blank)
cv.waitKey(0)
#write text
cv.putText(blank,'Hello',(300,300),cv.FONT_HERSHEY_TRIPLEX,2.0,(120,87,63),5)
cv.imshow('text',blank)
cv.waitKey(0)