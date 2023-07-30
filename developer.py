from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Developer window")

if __name__=="__main__": 
    root=Tk()
    obj=Developer(root)
    root.mainloop()