import cv2 as cv
import numpy as np
import os
#gathering directory, trained ai model and training data 
haar = cv.CascadeClassifier('haar_face_detector.xml')
people = ['Ad-deen01','Ad-deen02','Ad-deen03','Ad-deen04']
# file_path = r'E:\Python workspace\Imageprocessingpractise\Face_recognition_samples'
# for person in os.listdir(r'E:\Python workspace\Imageprocessingpractise\Face_recognition_samples'):
#     people.append(person)

features = np.load('Face_trainer.npy', allow_pickle= True)
Marking = np.load('Labelling.npy')

face_recognizing_ai_model = cv.face.LBPHFaceRecognizer_create()
face_recognizing_ai_model.read('Face_recognizing_model2.yml')

# #testing phase of a given image
# img = cv.imread(r'E:\Python workspace\Imageprocessingpractise\Face_recognition_samples\Somrat\90068878_856519421481218_357702713410060288_n.jpg')
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Unidentified',img)

# face_grabber = haar.detectMultiScale(grey, 1.1,4)       #grabbing the image for detection
# for (x,y,w,h) in face_grabber:
#     face_roi = grey[y:y+h,x:x+w]
#     label , confidence = face_recognizing_ai_model.predict(face_roi)
#     confidence = 100 - confidence
#     print(f'This is the face of {people[label]} with confidence {confidence}%')
#     cv.putText(img , str(f'Face of {people[label]} with Confidence = {confidence}'),(x,y-5),cv.FONT_HERSHEY_COMPLEX,.5,(0,255,0),1)
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
# cv.imshow('Detected image',img)
# cv.waitKey(0)


#testing phase of a given video
capture = cv.VideoCapture(0)
while True:
    isTrue , frame = capture.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #cv.imshow('crowd', grey)
    face_grabber = haar.detectMultiScale(grey, 1.1,4)
    for (x,y,w,h) in face_grabber:
        face_roi = grey[y:y+h,x:x+w]
        label , confidence = face_recognizing_ai_model.predict(face_roi)
        confidence = 100 - confidence
        #print(f'This is the face of {people[label]} with confidence {confidence}%')
        cv.putText(frame , str(f'Face of {people[label]} with Confidence = {confidence}'),(x,y-5),cv.FONT_HERSHEY_COMPLEX,.5,(0,255,0),1)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
     
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
capture.release() 
cv.destroyAllWindows() 

