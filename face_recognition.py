from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import numpy as np
import mysql.connector
import cv2
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Window")

        #Background image
        bgimgurl=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\faceRecog.jpg")
        bgimgurl=bgimgurl.resize((1280,650))
        self.backgroundimg=ImageTk.PhotoImage(bgimgurl)

        bgimg=Label(self.root,image=self.backgroundimg)
        bgimg.place(x=0,y=0,width=1280,height=650)

        b6_6=Button(self.root,text="Face Recognize",command=self.face_recog,cursor="hand2",
                    font=("times new roman",15,"bold"),bg="wheat",fg="blue")
        b6_6.place(x=100,y=300,width=400,height=100)

    # ======================= attendence ==============
    def mark_attendence(self,i,n,d):
        try:
            # # Connect to the database
            # conn = mysql.connector.connect(
            #     host="localhost",
            #     username="root",
            #     password="alok2565,",
            #     database="face_recognition"
            # )
            # my_cursor = conn.cursor()

            # # Fetch the current attendance count for the student
            # my_cursor.execute("SELECT att_count FROM student WHERE student_id=%s", (id,))
            # current_attendance_count = my_cursor.fetchone()[0]
            # new_attendance_count = current_attendance_count + 1

            with open("datafile.csv","r+",newline="\n") as f:
                mydataList = f.readlines()
                name_list=[]
                for line in mydataList:
                    entry=line.split((','))
                    name_list.append(entry[0])

                if((i not in name_list) and (n not in name_list) and (d not in name_list)):
                    now=datetime.now()
                    dt=now.strftime("%d/%m/%Y")
                    dtstring=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{n},{d},{dtstring},{dt},Present")

            # # Update the attendance count in the database
            # my_cursor.execute("UPDATE student SET att_count=%s WHERE student_id=%s", (new_attendance_count, id))
            # conn.commit()
            # conn.close()

            # print(f"Attendance marked for student with ID {id}. New attendance count: {new_attendance_count}")

        except Exception as e:
            print(f"Error while marking attendance: {e}")
        


        # =================== face recognition function ===========

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id = clf.predict(gray_image[y:y+h,x:x+w])[0]
                confidence = int((100*(1-id/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where student_id="+str(id))
                fetched_name=my_cursor.fetchone()
                if fetched_name is not None and isinstance(fetched_name, (list, tuple)):
                    fetched_name = "+".join(fetched_name)
                else:
                    fetched_name = ""

                #fetched_name="+".join(fetched_name)

                my_cursor.execute("select Dep from student where student_id="+str(id))
                fetched_dep=my_cursor.fetchone()
                if fetched_dep is not None and isinstance(fetched_dep, (list, tuple)):
                    fetched_dep = "+".join(fetched_dep)
                else:
                    fetched_dep = ""
                #fetched_dep="+".join(fetched_dep)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                fetched_id=my_cursor.fetchone()
                if fetched_id is not None:
                    fetched_id = [str(id) for id in fetched_id]
                    fetched_id = "+".join(fetched_id)
                else:
                    fetched_id = ""

                my_cursor.execute("select att_count from student where student_id="+str(id))
                att_count=my_cursor.fetchone()


                if confidence>77:
                    print(fetched_name," ", fetched_id," ",fetched_dep)
                    cv2.putText(img,f"Name:{fetched_name}"
                                    ,(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student Id:{fetched_id}"
                                    ,(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{fetched_dep}"
                                    ,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    self.mark_attendence(fetched_id,fetched_name,fetched_dep)
                    
                        
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face"
                                    ,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        
                coord=[x,y,w,h]
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("trainedFile.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break

        videoCap.release()
        cv2.destroyAllWindows()
                        
                         

                

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()