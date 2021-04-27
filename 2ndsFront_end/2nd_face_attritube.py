import tkinter
import os
from tkinter import messagebox
win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='lightpink'

def first():
    #execfile("N:\011project_solo\color_detection\2nd page_final.py")
    filename = 'N:\011project_solo\color_detection\2nd page_final.py'
    os.system(filename) 


a80=tkinter.Label(win,text="WELCOME")

a80.place(x=500,y=100, height=60,width=500)
a80['fg']="Red"
a80.config(font=("Courier", 50,"bold"))
a80['bg']='lightpink'

a81=tkinter.Label(win,text="What You Want To Do.\nHere is The List."
                 )

a81.place(x=500,y=150, height=200,width=600)
a81['bg']='lightpink'
a81['fg']="Green"
a81.config(font=("Courier", 35,"bold"))

a82=tkinter.Label(win,text="1. Image attribute(age,gender etc).")
a82.place(x=150,y=350, height=100,width=700)
b82 = tkinter.Button(text = "Go",command = first ,activeforeground = "red",activebackground = "pink",pady=10)
b82.place(x=1050,y=370, height=40,width=110)

a82['bg']='lightpink'
b82['fg']="blue"
a82.config(font=("Georgie", 30,"bold"))
b82['bg']='lightyellow'
b82.config(font=("Courier", 20,"bold"))


a83=tkinter.Label(win,text="2. Live-face attribute(age,gender etc)  .")
a83.place(x=150,y=450, height=100,width=790)
b83 = tkinter.Button(text = "Go",command = "",activeforeground = "red",activebackground = "pink",pady=10)
b83.place(x=1050,y=470, height=40,width=110)


a83['bg']='lightpink'
b83['bg']='lightyellow'
b83['fg']="blue"
a83.config(font=("Georgie", 30,"bold"))
b83.config(font=("Courier", 20,"bold"))


