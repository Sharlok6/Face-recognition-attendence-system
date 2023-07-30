from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import numpy as np
import mysql.connector
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendence system")

        title_lbl=Label(self.root,text="TRAIN DATA SET"
                        ,font=("times new roman",40,"bold")
                        ,bg="wheat",fg="red",compound="center")
        title_lbl.place(x=0,y=0,width=1280,height=130)

        b6_6=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",
                    font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=0,y=325,width=1260,height=40)

    def train_classifier(self):
        data_dir=("data")
        #this is called least comprehension. took data from our dir to file
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #converting image into gray scale
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13 #iska mtlb enter press krne ke badd window close ho jati h

        ids=np.array(ids)

        # ============= Train classifier ==============
        classifier=cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,ids)
        classifier.write("trainedFile.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!")


if __name__=="__main__":
    #We used tk module through root and then passed root into 
    root=Tk()
    obj=Train(root)
    root.mainloop()