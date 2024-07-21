from tkinter.ttk import *
from tkinter import *
import time

def present_time( ):
    current_time=time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000,present_time)
    
root=Tk()


root.title("Digital clock")

clock_label =Label(root,text="",font=("ds-digital",50),background="black",foreground="blue")
clock_label.pack(padx=20,pady=20)

present_time()
root.mainloop()