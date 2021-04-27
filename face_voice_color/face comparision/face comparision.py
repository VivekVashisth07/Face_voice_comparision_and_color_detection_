import cv2
import sys
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import PIL

from PIL import Image, ImageTk


#imagePath = sys.argv[1]
def original_face_image():
     root = Tk()
     root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
     global image1
     image1 = cv2.imread(root.filename)

     '''

     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
     faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.3,
         minNeighbors=11,
         minSize=(110,110)
         )



     for (x, y, w, h) in faces:
         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
         roi_color = image[y:y + h, x:x + w]
    
         cv2.imwrite('original_faces.jpg', roi_color)

     status = cv2.imwrite('faces_detected.jpg', image)
     print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
     
     '''
def getFaceBox1(net, frame, conf_threshold=0.7):
     frameOpencvDnn1 = frame.copy()
     frameHeight = frameOpencvDnn1.shape[0]
     frameWidth = frameOpencvDnn1.shape[1]
     blob = cv2.dnn.blobFromImage(frameOpencvDnn1, 1.0, (300, 300), [104, 117, 123], True, False)

     net.setInput(blob)
     detections = net.forward()
     #global bboxes1
     bboxes1 = []
     for i in range(detections.shape[2]):
          confidence = detections[0, 0, i, 2]
          if confidence > conf_threshold:
               x1 = int(detections[0, 0, i, 3] * frameWidth)
               y1 = int(detections[0, 0, i, 4] * frameHeight)
               x2 = int(detections[0, 0, i, 5] * frameWidth)
               y2 = int(detections[0, 0, i, 6] * frameHeight)
               bboxes1.append([x1, y1, x2, y2])
               cv2.rectangle(frameOpencvDnn1, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
                
     return frameOpencvDnn1, bboxes1



def image_to_compare():
     root = Tk()
     root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
     global image2
     image2 = cv2.imread(root.filename)
 
     '''

     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
     faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.3,
         minNeighbors=11,
         minSize=(110,110)
         )



     for (x, y, w, h) in faces:
         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
         roi_color = image[y:y + h, x:x + w]
     
         cv2.imwrite('image_to_compare.jpg', roi_color)

     status = cv2.imwrite('faces_detected.jpg', image)
     print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
    
     image_to_compare = cv2.imread(r"image_to_compare.jpg")



     '''
def getFaceBox2(net, frame, conf_threshold=0.7):
     frameOpencvDnn2 = frame.copy()
     frameHeight = frameOpencvDnn2.shape[0]
     frameWidth = frameOpencvDnn2.shape[1]
     blob = cv2.dnn.blobFromImage(frameOpencvDnn2, 1.0, (300, 300), [104, 117, 123], True, False)

     net.setInput(blob)
     detections = net.forward()
     #global bboxes2
     bboxes2 = []
     for i in range(detections.shape[2]):
          confidence = detections[0, 0, i, 2]
          if confidence > conf_threshold:
               x1 = int(detections[0, 0, i, 3] * frameWidth)
               y1 = int(detections[0, 0, i, 4] * frameHeight)
               x2 = int(detections[0, 0, i, 5] * frameWidth)
               y2 = int(detections[0, 0, i, 6] * frameHeight)
               bboxes2.append([x1, y1, x2, y2])
               cv2.rectangle(frameOpencvDnn2, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
                
     return frameOpencvDnn2, bboxes2


def face_comparision():
     import cv2
     import numpy as np

     faceProto="opencv_face_detector.pbtxt"
     faceModel="opencv_face_detector_uint8.pb"
     faceNet=cv2.dnn.readNet(faceModel,faceProto)
     MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
     
     #original1=getFaceBox1(faceNet,image1)
     #image_to_compare1=getFaceBox2(faceNet,image2)
     original1= cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
     original = faceCascade.detectMultiScale(
         original1,
         scaleFactor=1.3,
         minNeighbors=11,
         minSize=(110,110)
         )

     image_to_compare1= cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
     image_to_compare = faceCascade.detectMultiScale(
         image_to_compare1,
         scaleFactor=1.3,
         minNeighbors=11,
         minSize=(110,110)
         )


     #imagee1=PIL.Image.open("faces_detected.jpg")
     #photo_imagee1=ImageTk.PhotoImage(imagee1)
     '''
     a33=tkinter.Label(win, image=photo_imagee1)
     #label.pack()

     a33.place(x=600,y=600, height=600,width=600)
     a33['fg']="red"
     a33.config(font=("Courier", 22,"bold"))
     a33['bg']='red'
     '''
     
      
     #original=cv2.imread(r"original_faces.jpg")
     #image_to_compare = cv2.imread(r"image_to_compare.jpg")
     # 1) Check if 2 images are equals
     if original.shape == image_to_compare.shape:
         print("The images have same size and channels")
         difference = cv2.subtract(original, image_to_compare)
         b, g, r = cv2.split(difference)

         if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
             print("The images are completely Equal")
         else:
             print("The images are NOT equal")

     # 2) Check for similarities between the 2 images
     sift = cv2.SIFT_create()
     kp_1, desc_1 = sift.detectAndCompute(original, None)
     kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

     index_params = dict(algorithm=0, trees=5)
     search_params = dict()
     flann = cv2.FlannBasedMatcher(index_params, search_params)

     matches = flann.knnMatch(desc_1, desc_2, k=2)

     good_points = []
     for m, n in matches:
         if m.distance < 0.6*n.distance:
             good_points.append(m)

     # Define how similar they are
     number_keypoints = 0
     if len(kp_1) <= len(kp_2):
         number_keypoints = len(kp_1)
     else:
         number_keypoints = len(kp_2)

     
     print("Keypoints 1ST Image: " + str(len(kp_1)))
     print("Keypoints 2ND Image: " + str(len(kp_2)))
     print("GOOD Matches:", len(good_points))
     
     print("How good it's the match: ", len(good_points) / number_keypoints*100 )
     #messagebox.showinfo('RESULT', matchh )

     result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)


     global matchresult
     matchresult=len(good_points) / number_keypoints*100

     matchresult1='The Match Result Is:- ' , matchresult , ' %'
     a23=tkinter.Label(win,text= matchresult1)
     a23.place(x=200,y=600, height=50,width=900)
     a23['bg']='lightyellow'
     a23['fg']="green"
     a23.config(font=("Courier", 15,"bold"))
    
     cv2.imshow("result", cv2.resize(result, None, fx=0.8, fy=0.8))
     
     #cv2.imwrite("feature_matching.jpg", result)


     #cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
     #cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
     cv2.waitKey(0)
     cv2.destroyAllWindows()

win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='plum1'
a40=tkinter.Label(win,text="FACE \nMATCHING/COMPARISION")

a40.place(x=300,y=10, height=200,width=800)
a40['fg']="blue2"
a40.config(font=("Courier", 22,"bold"))
a40['bg']='plum1'

a41=tkinter.Label(win,text="Load the Original Image here")
a41.place(x=200,y=150, height=100,width=400)
b41 = tkinter.Button(text = "Click Here",command = original_face_image ,activeforeground = "red",activebackground = "pink",pady=10)
b41.place(x=300,y=250, height=40,width=200)

a41['bg']='plum1'
b41['fg']="dodgerblue"
a41.config(font=("Georgie", 20,"bold"))
b41['bg']='lightyellow'
b41.config(font=("Courier", 15,"bold"))

a42=tkinter.Label(win,text="Load the another Image here")
a42.place(x=700,y=150, height=100,width=500)
b42 = tkinter.Button(text = "Click Here",command = image_to_compare ,activeforeground = "red",activebackground = "pink",pady=10)
b42.place(x=820,y=250, height=40,width=200)

a42['bg']='plum1'
b42['fg']="dodgerblue"
a42.config(font=("Georgie", 20,"bold"))
b42['bg']='lightyellow'
b42.config(font=("Courier", 15,"bold"))

b42 = tkinter.Button(text = "Go",command = face_comparision ,activeforeground = "red",activebackground = "pink",pady=10)
b42.place(x=600,y=500, height=40,width=100)
b42['bg']='lightyellow'
b42['fg']="red"
b42.config(font=("Courier", 15,"bold"))




