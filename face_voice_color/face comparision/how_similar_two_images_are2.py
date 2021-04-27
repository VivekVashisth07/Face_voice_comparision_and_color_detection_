import cv2
import numpy as np
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

def original_Pic():
    
   
    global filename1
    filename1 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    
    
def compare_Pic():
    
    
    global filename2
    filename2 =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    


def twentyone():
    original = cv2.imread(filename1)
    image_to_compare = cv2.imread(filename2)


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


    #print("Keypoints 1ST Image: " + str(len(kp_1)))
    #print("Keypoints 2ND Image: " + str(len(kp_2)))
    #print("GOOD Matches:", len(good_points))
    #print("How good it's the match: ", len(good_points) / number_keypoints*100 )
    global matchresult
    matchresult=len(good_points) / number_keypoints*100

    matchresult1='The Match Result Is:- ' , matchresult , ' %'
    a23=tkinter.Label(win,text= matchresult1)
    a23.place(x=200,y=600, height=50,width=900)
    a23['bg']='lightyellow'
    a23['fg']="green"
    a23.config(font=("Courier", 15,"bold"))

    
    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
    
    messagebox.showinfo('Matching Result is ', matchresult1)
    cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
    
    #cv2.imwrite("feature_matching.jpg", result)


    #cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
    #cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
    cv2.waitKey(0)
    cv2.destroyAllWindows()






win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='plum1'
a30=tkinter.Label(win,text="IMAGE \nMATCHING/COMPARISION")

a30.place(x=300,y=50, height=200,width=800)
a30['fg']="blue2"
a30.config(font=("Courier", 22,"bold"))
a30['bg']='plum1'

a31=tkinter.Label(win,text="Load the Original Image here")
a31.place(x=200,y=250, height=100,width=400)
b31 = tkinter.Button(text = "Click Here",command = original_Pic ,activeforeground = "red",activebackground = "pink",pady=10)
b31.place(x=300,y=350, height=40,width=200)

a31['bg']='plum1'
b31['fg']="dodgerblue"
a31.config(font=("Georgie", 20,"bold"))
b31['bg']='lightyellow'
b31.config(font=("Courier", 15,"bold"))

a32=tkinter.Label(win,text="Load the another Image here")
a32.place(x=700,y=250, height=100,width=500)
b32 = tkinter.Button(text = "Click Here",command = compare_Pic ,activeforeground = "red",activebackground = "pink",pady=10)
b32.place(x=820,y=350, height=40,width=200)

a32['bg']='plum1'
b32['fg']="dodgerblue"
a32.config(font=("Georgie", 20,"bold"))
b32['bg']='lightyellow'
b32.config(font=("Courier", 15,"bold"))

b32 = tkinter.Button(text = "Go",command = twentyone ,activeforeground = "red",activebackground = "pink",pady=10)
b32.place(x=600,y=500, height=40,width=100)
b32['bg']='lightyellow'
b32['fg']="red"
b32.config(font=("Courier", 15,"bold"))

