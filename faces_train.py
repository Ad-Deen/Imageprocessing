import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os 

# people = []
# file_path = r'E:\Python workspace\Imageprocessingpractise\Face_recognition_samples'
# for person in os.listdir(r'E:\Python workspace\Imageprocessingpractise\Face_recognition_samples'):
#     people.append(person)
    
# print(people)
haar = cv.CascadeClassifier('haar_face_detector.xml')
Face_train = []
labels = []
#creating the face grabbing function to create training data from various directories images
# def Create_train():
#     for person in people:           #allocating image folder path
#         path = os.path.join(file_path,person)       #extending the path towards img folders from main folder
#         label = people.index(person)                #labeling origin
#         for img in os.listdir(path):                #extending the path upto image to use to read and detect the face
#             img_path = os.path.join(path , img)
#             img_array = cv.imread(img_path)
#             gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
#             face_grabber = haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
            
#             for (x,y,i,j) in face_grabber:             #grabbing the face along with labelling them and creating the training data set where each image has correspondance to labels
#                 faces_roi = gray[y:y+j,x:x+i]
#                 Face_train.append(faces_roi)
#                 labels.append(label)
# Face_train = np.array(Face_train,dtype = 'object')
# labels= np.array(labels)


# print(f'Number of face models = {len(Face_train)}')
# print(f'Number of labels = {len(labels)}')
# # #creating the face recognizing model
# face_recognizing_ai_model = cv.face.LBPHFaceRecognizer_create()
# face_recognizing_ai_model.train(Face_train,labels)
# np.save('Face_trainer2.npy',Face_train)
# np.save('Labelling2.npy',labels)
# face_recognizing_ai_model.save('Face_recognizing_model2.yml')
# # print("training done ------------")
# print(labels)

                
#Face training using video
capture = cv.VideoCapture(0)
label = 0
while True:
    isTrue , frame = capture.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_grabber = haar.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=8)
        
    for (x,y,i,j) in face_grabber:             #grabbing the face along with labelling them and creating the training data set where each image has correspondance to labels
        faces_roi = grey[y:y+j,x:x+i]
        cv.imshow('point of interest',faces_roi)
        Face_train.append(faces_roi)
        labels.append(label)
        
        #cv.imshow('Video',frame)
        
        if cv.waitKey(20) & 0xFF==ord('n'):
            label = label + 1
            cv.waitKey(5000)
        # if cv.waitKey(0) & 0xFF==ord('n'):
        #     cv.waitKey(20)
    if cv.waitKey(20) & 0xFF==ord('d'):
            break
capture.release() 
cv.destroyAllWindows()  


Face_train = np.array(Face_train,dtype = 'object')
labels= np.array(labels)


print(f'Number of face models = {len(Face_train)}')
print(f'Number of labels = {len(labels)}')
# #creating the face recognizing model
face_recognizing_ai_model = cv.face.LBPHFaceRecognizer_create()
face_recognizing_ai_model.train(Face_train,labels)
np.save('Face_trainer2.npy',Face_train)
np.save('Labelling2.npy',labels)
face_recognizing_ai_model.save('Face_recognizing_model2.yml')
# print("training done ------------")
print(labels)

            