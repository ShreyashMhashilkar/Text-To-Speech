import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speak():
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

text=StringVar()

obj=LabelFrame(root,text="Text to speech",font=25,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

label=Label(obj,text="Text",font=30)
label.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=text,font=30,width=35,bd=5)
text.pack(side=tk.LEFT,padx=10)

button = Button(obj,text="Speak",font=20,bg="yellow",fg="black",command=speak)
button.pack(side=tk.LEFT,padx=10)

root.title("Convert Text To Speech")
root.geometry("600x300")
root.resizable(False,False)
root.mainloop()
