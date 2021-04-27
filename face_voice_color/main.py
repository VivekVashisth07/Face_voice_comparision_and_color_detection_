import tkinter
import os
from tkinter import messagebox
win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='lightskyblue'

def second():
    #execfile("N:\011project_solo\color_detection\2nd page_final.py")
    #filename = 'N:\011project_solo\color_detection\2nd page_final.py'
    os.system('2nd_image_compare.py') 


a0=tkinter.Label(win,text="WELCOME")

a0.place(x=500,y=100, height=60,width=500)
a0['fg']="Red"
a0.config(font=("Courier", 50,"bold"))
a0['bg']='lightskyblue'

a1=tkinter.Label(win,text="What You Want To Do.\nHere is The List."
                 )

a1.place(x=500,y=150, height=200,width=600)
a1['bg']='lightskyblue'
a1['fg']="Green"
a1.config(font=("Courier", 35,"bold"))

a2=tkinter.Label(win,text="1. Color Recognition of an image.")
a2.place(x=100,y=350, height=100,width=700)
b2 = tkinter.Button(text = "Go",command = "" ,activeforeground = "red",activebackground = "pink",pady=10)
b2.place(x=1000,y=370, height=40,width=110)

a2['bg']='lightskyblue'
b2['fg']="blue"
a2.config(font=("Georgie", 30,"bold"))
b2['bg']='lightyellow'
b2.config(font=("Courier", 20,"bold"))


a3=tkinter.Label(win,text="2. Face/Image Matching of two person.")
a3.place(x=100,y=450, height=100,width=790)
b3 = tkinter.Button(text = "Go",command = second ,activeforeground = "red",activebackground = "pink",pady=10)
b3.place(x=1000,y=470, height=40,width=110)


a3['bg']='lightskyblue'
b3['bg']='lightyellow'
b3['fg']="blue"
a3.config(font=("Georgie", 30,"bold"))
b3.config(font=("Courier", 20,"bold"))


a4=tkinter.Label(win,text="3. Sound Matching of two sample of sound.")
a4.place(x=100,y=550, height=100,width=880)
b4 = tkinter.Button(text = "Go",command = "",activeforeground = "red",activebackground = "pink",pady=10)
b4.place(x=1000,y=570, height=40,width=110)

a4['bg']='lightskyblue'
b4['bg']='lightyellow'
b4['fg']="blue"
a4.config(font=("Georgie", 30,"bold"))
b4.config(font=("Courier", 20,"bold"))


a5=tkinter.Label(win,text="4.  Find Some Property of face.")
a5.place(x=100,y=650, height=100,width=650)
b5 = tkinter.Button(text = "Go",command = "",activeforeground = "red",activebackground = "pink",pady=10)
b5.place(x=1000,y=670, height=40,width=110)

a5['bg']='lightskyblue'
b5['bg']='lightyellow'
b5['fg']="blue"
a5.config(font=("Georgie", 30,"bold"))
b5.config(font=("Courier", 20,"bold"))

