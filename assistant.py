import random
import tkinter    
from tkinter import *
import datetime
import pyttsx3
import os
import time
import webbrowser
from PIL import ImageTk,Image

engine = pyttsx3.init()
window = Tk()

window.configure(bg = "black")
SET_WIDTH = 1200
SET_HEIGHT = 700

global ques

ques = Entry(window,width=40,bg="black",fg="white",font = ('arial',18,'bold'))   
ques.pack(padx = 10,pady = 20)

creator_name='Arjun'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    Hour_time=datetime.datetime.now().strftime("%H")
    Minutes=datetime.datetime.now().strftime("%M")
    if hour == 0 and hour<=12:
        speak(f"Good morning {creator_name} sir",f"The time is {Hour_time}{Minutes} AM")
    elif hour>=12 and hour<=18:
        speak(f"Good afternoon {creator_name} sir"f"The time is {Hour_time}{Minutes} PM")
    else:
        speak(f" Good evening {creator_name} sir"f"The time is {Hour_time}{Minutes} PM")
    speak("I'm your personal assistance sir!")
    speak("How may I help you?")


def command():
    if 'open file' in ques.get():
        speak("which file sir ")
        d = Toplevel()
        Toplevel.configure(d,bg="black")
        e = Entry(d,bg = "black", fg = "white" ,width = 20)
        e.pack()
        def open_file():
            if os.path.exists(e.get()):
                os.system(e.get())
                speak("Ok sir i will open "+e.get())
            else:
                speak("Sorry sir i can't open "+e.get())
        s = Button(d,bg = "black",font = ('arial',18,'bold'),fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_file).pack()

    elif 'shutdown' in ques.get():
        os.system("shutdown now -h")
        speak("ok sir i shutdown the computer")

    elif 'open stackoverflow' in ques.get():
        speak("ok sir i will open the stck over flow website")
        webbrowser.open("https://wwww.stackoverflow.com")

    elif 'open website' in ques.get():
        speak("which website sir ")
        d = Toplevel()
        e = Entry(d,bg = "black", fg = "white" ,font = ('arial',18,'bold'),width = 20)
        e.pack()
        def open_web():
            webbrowser.open("https://"+e.get()+".com")
            speak("ok sir i will open "+e.get())
        s = Button(d,bg = "black",fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_web).pack()

    elif 'open google' in ques.get():
        speak("ok sir i will open google.com")
        webbrowser.open("https://www.google.com")

    elif 'open youtube' in ques.get():
        speak("ok sir i will opwn youtube dot com")
        webbrowser.open("https://www.youtube.com")

    elif 'copy code' in ques.get():
        speak("of which file sir ")
        d = Toplevel()
        e = Entry(d,bg = "black",font = ('arial',18,'bold'), fg = "white" ,width = 20)
        e.pack()
        def open_code():
            file = open(e.get(),"r+")
            re = file.read()
            speak(re)
        s = Button(d,bg = "black",fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_code).pack()
        

    elif 'exit' in ques.get():
        speak("good bye sir have a good day")
        exit()

    elif 'quite' in ques.get():
        speak("good bye sir have a good day")
        exit() 

    else :
        speak("sorry sir i can not do this")

    
def win():
    speak("ok sir i will open the google")
    webbrowser.open("https://www.google.com")
 
def you():
    speak("ok sir open the youtube.com")
    webbrowser.open("https://www.youtube.com")


def main():
    # screen

    bgImg = Image.open("back2.png")
    window.title(f"J.A.R.V.I.S {creator_name}'s Personal Assistance")
    canvas = tkinter.Canvas(window,width = SET_WIDTH,height = SET_HEIGHT)

    image=ImageTk.PhotoImage(bgImg)
    canvas.create_image(0,0,anchor=NW,image=image)

    # entry
    btn = Button(bg = "black" ,fg = "white",width=20,activeforeground = "grey",activebackground = "black",text = "command",command=command).pack(pady = 0 , padx = 0)
    canvas.configure(bg="black")


    btn = Button(text = "Open google" ,bg = "black" ,fg="white",width=20,activeforeground = "grey",activebackground = "black",command = win)
    btn.pack(padx = 3,pady= 1,side = BOTTOM)

    btn = Button(text = " Open Youtube" ,bg = "black",fg = "white" ,width = 20,activeforeground  = "grey" ,activebackground = "black",command =you)
    btn.pack(side = BOTTOM)


    
    
    shape = canvas.create_oval(10,10,60,60,fill = "blue")
    xspeed = random.randrange(1,20)
    yspeed = random.randrange(1, 20)

    shape2 = canvas.create_oval(10,10,60,60,fill = "blue")
    xspeed2 = random.randrange(1,20)
    yspeed2 = random.randrange(1,20)

    canvas.pack()
    a=0
    while True:
        canvas.move(shape,xspeed,yspeed)
        pos = canvas.coords(shape)
        if pos[3]>= 700 or pos[1] <=0:
            yspeed = -yspeed
        if pos[2] >= 800 or pos[0] <=0:
            xspeed= -xspeed

        canvas.move(shape2,xspeed2,yspeed2)
        pos = canvas.coords(shape2)
        if pos[3]>= 700 or pos[1] <=0:
            yspeed2 = -yspeed2
        if pos[2] >= 800 or pos[0] <=0:
            xspeed2= -xspeed2                                
        window.update()
        time.sleep(0.01)
        if a==0:
            wish()
            a=1
def ball():
    canvas = Canvas()
    


if __name__ == "__main__":
    main()


window.mainloop()