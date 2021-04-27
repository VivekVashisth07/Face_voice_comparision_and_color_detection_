import cv2
import numpy as np
import pandas as pd
import argparse

import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *





class colorDetection():
    
    #Reading the image with opencv





    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.filename)
    global img
    img = cv2.imread(root.filename)


    #declaring global variables (are used later on)
    clicked = False
    r = g = b = xpos = ypos = 0

    #Reading csv file with pandas and giving names to each column
    index=["color","color_name","hex","R","G","B"]
    csv = pd.read_csv('colors.csv', names=index, header=None)

    #function to calculate minimum distance from all colors and get the most matching color
    def getColorName(R,G,B):
        minimum = 10000
        for i in range(len(csv)):
            d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
            if(d<=minimum):
                minimum = d
                print(d)
                cname = csv.loc[i,"color_name"]
                print(cname)
        return cname

    #function to get x,y coordinates of mouse double click
    def draw_function(event, x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            global b,g,r,xpos,ypos, clicked
            clicked = True
            xpos = x
            ypos = y
            b,g,r = img[y,x]
            b = int(b)
            g = int(g)
            r = int(r)
            print(x)
            print(y)
       
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_function)

    while(1):

        cv2.imshow("image",img)
        if (clicked):
   
            #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
            cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
            

            #Creating text string to display( Color name and RGB values )
            text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
            
            #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
    
            #For very light colours we will display text in black colour
            if(r+g+b>=600):
                cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
                
            clicked=False

        #Break the loop when user hits 'esc' key    
        if cv2.waitKey(20) & 0xFF ==27:
            break
    
    cv2.destroyAllWindows()

win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='lightskyblue'
a0=tkinter.Label(win,text="Here you load your image and\nAfter clicking double click.\nYou are able to see the clour name.\nPress esc to get out of it",justify=LEFT)

a0.place(x=100,y=100, height=200,width=800)
a0['fg']="Green"
a0.config(font=("Courier", 22,"bold"))
a0['bg']='lightskyblue'

a1=tkinter.Label(win,text="Load the Image here")
a1.place(x=100,y=350, height=100,width=500)
b1 = tkinter.Button(text = "Click Here",command = colorDetection ,activeforeground = "red",activebackground = "pink",pady=10)
b1.place(x=700,y=380, height=40,width=200)

a1['bg']='lightskyblue'
b1['fg']="blue"
a1.config(font=("Georgie", 30,"bold"))
b1['bg']='lightyellow'
b1.config(font=("Courier", 20,"bold"))
