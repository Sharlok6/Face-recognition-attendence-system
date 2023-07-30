from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
import os
import numpy as np
import cv2
from tkinter import messagebox
from time import strftime
from datetime import datetime
#import mysql.connector

class Face_Recognition_System:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendence system")

        #Background image
        bgimgurl=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\bg.jpg")
        bgimgurl=bgimgurl.resize((1280,650))
        self.backgroundimg=ImageTk.PhotoImage(bgimgurl)

        bgimg=Label(self.root,image=self.backgroundimg)
        bgimg.place(x=0,y=0,width=1280,height=650)

        title_lbl=Label(bgimg,text="FACE RECOGNITION ATTENDENCE SYSTEM"
                        ,font=("times new roman",40,"bold")
                        ,bg="wheat",fg="red",compound="center")
        title_lbl.place(x=0,y=0,width=1280,height=130)

        # ======== time =========
        def time():
            string =strftime('%H : %M : %S : %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='white',fg='blue')
        lbl.place(x=0,y=(-15),width=150,height=50)
        time()

        #student button
        stu_btn_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\details2.webp")
        stu_btn_url=stu_btn_url.resize((180,180))
        self.stu_btn_img=ImageTk.PhotoImage(stu_btn_url)

        b1=Button(bgimg,image=self.stu_btn_img,command=self.student_details,cursor="hand2")
        b1.place(x=80,y=150,width=180,height=180)

        b1_1=Button(bgimg,text="Student details",command=self.student_details,cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=80,y=335,width=180,height=40)

        #Check Attendence button
        check_btn_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\checkattendence.png")
        check_btn_url=check_btn_url.resize((180,180))
        self.check_btn_img=ImageTk.PhotoImage(check_btn_url)

        b3=Button(bgimg,image=self.check_btn_img,command=self.attendence,cursor="hand2")
        b3.place(x=400,y=150,width=180,height=180)

        b3_3=Button(bgimg,text="Check Attendence",command=self.attendence,cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=400,y=335,width=180,height=40)

        #Help desk button
        helpdesk_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\helpdesk.jpg")
        helpdesk_url=helpdesk_url.resize((180,180))
        self.helpdesk_img=ImageTk.PhotoImage(helpdesk_url)

        b4=Button(bgimg,image=self.helpdesk_img,cursor="hand2")
        b4.place(x=720,y=150,width=180,height=180)

        b4_4=Button(bgimg,text="Help desk",cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=720,y=335,width=180,height=40)

        #Detect face button
        detectface_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\detectface.webp")
        detectface_url=detectface_url.resize((180,180))
        self.detectface_img=ImageTk.PhotoImage(detectface_url)

        b2=Button(bgimg,image=self.detectface_img,cursor="hand2",command=self.face_data)
        b2.place(x=80,y=390,width=180,height=180)

        b2_2=Button(bgimg,text="Detect Face",cursor="hand2",command=self.face_data,
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=80,y=580,width=180,height=40)

        #Train face button
        Trainface_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\trainface.jpg")
        Trainface_url=Trainface_url.resize((180,180))
        self.Trainface_img=ImageTk.PhotoImage(Trainface_url)

        b5=Button(bgimg,image=self.Trainface_img,cursor="hand2",command=self.train_data)
        b5.place(x=400,y=390,width=180,height=180)

        b5_5=Button(bgimg,text="Train Face",cursor="hand2",command=self.train_data,
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=400,y=580,width=180,height=40)

        #Photos button
        Photos_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\photos.png")
        Photos_url=Photos_url.resize((180,180))
        self.Photos_img=ImageTk.PhotoImage(Photos_url)

        b6=Button(bgimg,image=self.Photos_img,cursor="hand2",command=self.open_img)
        b6.place(x=720,y=390,width=180,height=180)

        b6_6=Button(bgimg,text="Photos",cursor="hand2",command=self.open_img,
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=720,y=580,width=180,height=40)

        #Developer button
        Dev_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\dev.jpg")
        Dev_url=Dev_url.resize((180,180))
        self.Dev_img=ImageTk.PhotoImage(Dev_url)

        b7=Button(bgimg,image=self.Dev_img,cursor="hand2")
        b7.place(x=1040,y=150,width=180,height=180)

        b7_7=Button(bgimg,text="Developer",cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=1040,y=335,width=180,height=40)

        #Exit button
        exit_url=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\exit.webp")
        exit_url=exit_url.resize((180,180))
        self.exit_img=ImageTk.PhotoImage(exit_url)

        b8=Button(bgimg,image=self.exit_img,cursor="hand2")
        b8.place(x=1040,y=390,width=180,height=180)

        b8_8=Button(bgimg,text="Exit",cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1040,y=580,width=180,height=40)

    # ============== For opening images in folder =============
    def open_img(self):
        os.startfile("data")

    # ============== Functions Button ============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # ============== Train data set Button ============
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    # ============= Face recognition ==============
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    # ============= Attendence details =============
    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)



if __name__=="__main__":
    #We used tk module through root and then passed root into 
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

