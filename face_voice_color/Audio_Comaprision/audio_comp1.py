import wave
import numpy as np
import matplotlib.pyplot as plt
import librosa

'''
Only support wav
'''


import cv2
import numpy as np
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

def original_audio():
    
   
    global filename11
    filename11 =  filedialog.askopenfilename(initialdir = "/",title = "Select file only .wav",filetypes = (("Audio Files", ".wav .ogg"),("all files","*.*")))
    
    
def compare_audio():
    
    
    global filename12
    filename12 =  filedialog.askopenfilename(initialdir = "/",title = "Select file only .wav",filetypes = (("Audio Files", ".wav .ogg"),("all files","*.*")))
    


def thirtyone():

    wave_data1, samplerate1=librosa.load(filename11)
    pitches1, magnitudes1 = librosa.piptrack(y=wave_data1, sr=samplerate1)
    plt.plot(pitches1)
    
    #plt.show()
    #print(pitches1.sum())
    #print(samplerate1)


    wave_data2, samplerate2=librosa.load(filename12)
    pitches2, magnitudes2 = librosa.piptrack(y=wave_data2, sr=samplerate2)

    plt.plot(pitches2)
    #plt.show()
    #print(pitches2.sum())
    #print(samplerate2)
    diff=(pitches1.sum()/pitches2.sum())*100
    print(diff)

    


    

    matchresult1='The Match Result Is:- ' , diff , ' %'
    a23=tkinter.Label(win,text= matchresult1)
    a23.place(x=200,y=600, height=50,width=900)
    a23['bg']='lightyellow'
    a23['fg']="green"
    a23.config(font=("Courier", 15,"bold"))





win= tkinter.Tk()
win.minsize(1080,720)
win['bg']='lightgreen'
a30=tkinter.Label(win,text="Audio \nMATCHING/COMPARISION")

a30.place(x=300,y=50, height=200,width=800)
a30['fg']="blue2"
a30.config(font=("Courier", 22,"bold"))
a30['bg']='lightgreen'

a31=tkinter.Label(win,text="Load the Original(.wav) Audio here")
a31.place(x=200,y=250, height=100,width=500)
b31 = tkinter.Button(text = "Click Here",command = original_audio ,activeforeground = "red",activebackground = "pink",pady=10)
b31.place(x=300,y=350, height=40,width=200)

a31['bg']='lightgreen'
b31['fg']="dodgerblue"
a31.config(font=("Georgie", 20,"bold"))
b31['bg']='lightyellow'
b31.config(font=("Courier", 15,"bold"))

a32=tkinter.Label(win,text="Load the another(.wav) Audio here")
a32.place(x=700,y=250, height=100,width=600)
b32 = tkinter.Button(text = "Click Here",command = compare_audio ,activeforeground = "red",activebackground = "pink",pady=10)
b32.place(x=820,y=350, height=40,width=200)

a32['bg']='lightgreen'
b32['fg']="dodgerblue"
a32.config(font=("Georgie", 20,"bold"))
b32['bg']='lightyellow'
b32.config(font=("Courier", 15,"bold"))

b32 = tkinter.Button(text = "Go",command = thirtyone ,activeforeground = "red",activebackground = "pink",pady=10)
b32.place(x=600,y=500, height=40,width=100)
b32['bg']='lightyellow'
b32['fg']="red"
b32.config(font=("Courier", 15,"bold"))

