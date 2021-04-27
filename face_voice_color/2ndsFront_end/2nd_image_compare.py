import tkinter
import os
from tkinter import messagebox
win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='yellow2'

def first():
    #execfile("N:\011project_solo\color_detection\2nd page_final.py")
    filename = 'N:\011project_solo\color_detection\2nd page_final.py'
    os.system(filename) 


a90=tkinter.Label(win,text="WELCOME")

a90.place(x=500,y=100, height=60,width=500)
a90['fg']="Red"
a90.config(font=("Courier", 50,"bold"))
a90['bg']='yellow2'

a91=tkinter.Label(win,text="What You Want To Do.\nHere is The List."
                 )

a91.place(x=500,y=150, height=200,width=600)
a91['bg']='yellow2'
a91['fg']="Green"
a91.config(font=("Courier", 35,"bold"))

a92=tkinter.Label(win,text="1. Image Compare with another. ")
a92.place(x=150,y=350, height=100,width=700)
b92 = tkinter.Button(text = "Go",command = first ,activeforeground = "red",activebackground = "pink",pady=10)
b92.place(x=1050,y=370, height=40,width=110)

a92['bg']='yellow2'
b92['fg']="blue"
a92.config(font=("Georgie", 30,"bold"))
b92['bg']='lightyellow'
b92.config(font=("Courier", 20,"bold"))


a93=tkinter.Label(win,text="2. Face compare with aother.")
a93.place(x=150,y=450, height=100,width=630)
b93 = tkinter.Button(text = "Go",command = "",activeforeground = "red",activebackground = "pink",pady=10)
b93.place(x=1050,y=470, height=40,width=110)


a93['bg']='yellow2'
b93['bg']='lightyellow'
b93['fg']="blue"
a93.config(font=("Georgie", 30,"bold"))
b93.config(font=("Courier", 20,"bold"))


