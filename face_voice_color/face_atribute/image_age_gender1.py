#Using sample image
#import AgeGender
#python AgeGender.py --input sample1.jpg
import cv2
import math
import numpy as np
import pandas as pd
import argparse
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
def fiftyone():
    
    root = Tk()
    root.filename51 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    img = cv2.imread( root.filename51)
    def getFaceBox(net, frame, conf_threshold=0.7):
        frameOpencvDnn = frame.copy()
        frameHeight = frameOpencvDnn.shape[0]
        frameWidth = frameOpencvDnn.shape[1]
        blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

        net.setInput(blob)
        detections = net.forward()
        #global bboxes
        bboxes = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                bboxes.append([x1, y1, x2, y2])
                cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)

        return frameOpencvDnn, bboxes
    faceProto="opencv_face_detector.pbtxt"
    faceModel="opencv_face_detector_uint8.pb"
    genderProto = "gender_deploy.prototxt"
    genderModel = "gender_net.caffemodel"
    ageProto="age_deploy.prototxt"
    ageModel="age_net.caffemodel"
    MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)

    faceNet=cv2.dnn.readNet(faceModel,faceProto)


    ageNet = cv2.dnn.readNet(ageModel, ageProto)

    genderNet=cv2.dnn.readNet(genderModel,genderProto)
    genderList = ['Male', 'Female']
    padding=20
    resultImg,bboxes=getFaceBox(faceNet,img)
    #face=frame[max(0,faceBox[1]-padding):
    #                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
    #                     :min(faceBox[2]+padding, frame.shape[1]-1)]

    blob = cv2.dnn.blobFromImage(resultImg, 10, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    #print("Gender Output : {}".format(genderPreds))
    print(f"Gender : {gender}")



    ageProto = "age_deploy.prototxt"
    ageModel = "age_net.caffemodel"
    ageNet = cv2.dnn.readNet(ageModel, ageProto)

    ageList = ['(0 - 2)', '(4 - 6)', '(8 - 12)', '(15 - 20)', '(25 - 32)', '(38 - 43)', '(48 - 53)', '(60 - 100)']

    ageNet.setInput(blob)
    agePreds = ageNet.forward()
    age = ageList[agePreds[0].argmax()]
    print("Gender Output : {}".format(agePreds))
    print(f'Age: {age[1:-1]} years')
    print(age)
    print(gender)
    


    label = "{}, {}".format(gender, age)
    cv2.putText(resultImg, f'{gender}, {age}', (50,50),2,0.8,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow("Age Gender Demo", resultImg)


    



win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='black'
a50=tkinter.Label(win,text="Here you load your image and\nAfter uploading you able to see.\nimage face,age,gender etc.",justify=LEFT)

a50.place(x=200,y=100, height=180,width=800)
a50['fg']="green"
a50.config(font=("Courier", 22,"bold"))
a50['bg']='black'

a51=tkinter.Label(win,text="Load the Image here")
a51.place(x=200,y=300, height=100,width=500)
b51 = tkinter.Button(text = "Click Here",command = fiftyone ,activeforeground = "red",activebackground = "pink",pady=10)
b51.place(x=700,y=330, height=40,width=200)

a51['bg']='black'
a51['fg']="plum1"
b51['fg']="dodgerblue"
a51.config(font=("Georgie", 30,"bold"))
b51['bg']='lightyellow'
b51.config(font=("Courier", 20,"bold"))


