import cv2 as cv
import numpy as np

img = cv.imread('Sample images and videos\Scene.jpg')
# print(img.shape)
cv.imshow('nature',img)

#Translation of images
def Translate(img , x , y ):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions,)

translated = Translate(img,100,150)
cv.imshow('translated',translated)

#rotation
# def rotate(img, angle, rotPoint=None):
#     (height,width) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2,height//2)
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1)
#     Dimensions = (width,height)
#     return cv.warpAffine(img, rotMat,Dimensions,)
# rotated = rotate(img,-45)
# cv.imshow('rotated',rotated)
# rotator = rotated
# i = -45
# j = 1
# while i>= -360 :
#     i = i - 5
#     strrot = "rotate" + str(j)
#     rotator = rotate(rotator, i)
#     cv.imshow(strrot,rotator)
#     j = j + 1
#     if cv.waitKey(500) & 0xFF == ord('d'):
#         break
#flipping the image
flipped = cv.flip(img,1)
cv.imshow('flipped',flipped)
       
      
cv.waitKey(0)