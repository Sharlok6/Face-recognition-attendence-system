from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Face recognition Attendence system")

        # ******* Variables for sending data to backend ***********
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_section=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_attendence_count=IntVar(value=0)

        #Background image
        bgimgurl=Image.open(r"C:\Users\hp\OneDrive\Desktop\Project for 6th sem\Images\bg.jpg")
        bgimgurl=bgimgurl.resize((1280,650))
        self.backgroundimg=ImageTk.PhotoImage(bgimgurl)

        bgimg=Label(self.root,image=self.backgroundimg)
        bgimg.place(x=0,y=0,width=1280,height=650)

        title_lbl=Label(bgimg,text="STUDENT DETAILS"
                        ,font=("times new roman",40,"bold")
                        ,bg="wheat",fg="red",compound="center")
        title_lbl.place(x=0,y=0,width=1280,height=130)

        main_frame=Frame(bgimg,bd=2)
        main_frame.place(x=15,y=140,width=1240,height=500)

        #left label frame
        leftframe=LabelFrame(main_frame,bd=2,bg="wheat",relief=RIDGE
                             ,text="Student details"
                             ,font=("times new roman",15,"bold"))
        leftframe.place(x=10,y=10,width=610,height=470)

        #current course
        currCourse=LabelFrame(leftframe,bd=2,bg="white",relief=RIDGE
                             ,text="Current course details"
                             ,font=("times new roman",12,"bold"))
        currCourse.place(x=10,y=5,width=590,height=120)

        # Department
        dept_label=Label(currCourse,text="Department",font=("serif",12,"bold"))
        dept_label.grid(row=0,column=0,padx=10)
        dept_combo=ttk.Combobox(currCourse,textvariable=self.var_dept,font=("serif",12),width=17,state="readonly")
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","Electrical","ECE","PIE")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=3,pady=10)

        # Course
        course_label=Label(currCourse,text="Course",font=("serif",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(currCourse,textvariable=self.var_course,font=("serif",12),width=17,state="readonly")
        course_combo["values"]=("Select Course","SE","OS","CN","Python")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

        # Year
        year_label=Label(currCourse,text="Year",font=("serif",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(currCourse,textvariable=self.var_year,font=("serif",12),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020","2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

        # Semester
        sem_label=Label(currCourse,text="Semester",font=("serif",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(currCourse,textvariable=self.var_sem,font=("serif",12),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)


        #Class Student information
        classStudent=LabelFrame(leftframe,bd=2,bg="white",relief=RIDGE
                             ,text="Class Student Information"
                             ,font=("times new roman",12,"bold"))
        classStudent.place(x=10,y=140,width=590,height=300)

        # Student Id
        studentId_label=Label(classStudent,text="Student Id",font=("serif",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(classStudent,textvariable=self.var_id,width=15,font=("serif",12))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        studentname_label=Label(classStudent,text="Student Name",font=("serif",12,"bold"))
        studentname_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        studentname_entry=ttk.Entry(classStudent,textvariable=self.var_name,width=15,font=("serif",12))
        studentname_entry.grid(row=0,column=3,padx=15,pady=5,sticky=W)

        # Section
        Section_label=Label(classStudent,text="Section",font=("serif",12,"bold"))
        Section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        #Section_entry=ttk.Entry(classStudent,textvariable=self.var_section,width=15,font=("serif",12))
        #Section_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(classStudent,textvariable=self.var_section,font=("serif",12),width=13,state="readonly")
        section_combo["values"]=("Select Section","A","B","C")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(classStudent,text="Gender",font=("serif",12,"bold"))
        gender_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        #gender_entry=ttk.Entry(classStudent,textvariable=self.var_gender,width=15,font=("serif",12))
        #gender_entry.grid(row=1,column=3,padx=15,pady=5,sticky=W)

        gender_combo=ttk.Combobox(classStudent,textvariable=self.var_gender,font=("serif",12),width=13,state="readonly")
        gender_combo["values"]=("male","female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=15,pady=5,sticky=W)

        # Email-Id
        emailId_label=Label(classStudent,text="Email-Id",font=("serif",12,"bold"))
        emailId_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        emailId_entry=ttk.Entry(classStudent,textvariable=self.var_email,width=15,font=("serif",12))
        emailId_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Phone No.
        PhoneNo_label=Label(classStudent,text="Phone No.",font=("serif",12,"bold"))
        PhoneNo_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        PhoneNo_entry=ttk.Entry(classStudent,textvariable=self.var_phone,width=15,font=("serif",12))
        PhoneNo_entry.grid(row=2,column=3,padx=15,pady=5,sticky=W)

        # Attendence count
        # Attendence_count_label=Label(classStudent,text="No. of Attendence:",font=("serif",12,"bold"))
        # Attendence_count_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        # Attendence_count_entry=ttk.Entry(classStudent,textvariable=self.var_attendence_count,width=15,font=("serif",12))
        # Attendence_count_entry.grid(row=3,column=1,padx=15,pady=5,sticky=W)

        # #radio buttons
        # self.var_radio1=StringVar()
        # radiobtn1=ttk.Radiobutton(classStudent,variable=self.var_radio1,text="Take photo sample",value="Yes")
        # radiobtn1.grid(row=4,column=0,padx=8,pady=5)

        # #self.var_radio2=StringVar()
        # radiobtn2=ttk.Radiobutton(classStudent,variable=self.var_radio1,text="No photo sample",value="No")
        # radiobtn2.grid(row=4,column=1,padx=8,pady=5)

        #buttons frame
        btn_frame=Frame(classStudent,bd=2,relief=RIDGE,bg="ghostwhite")
        btn_frame.place(x=10,y=150,width=565,height=50)

        # Save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12
                        ,font=("times new roman",13,"bold")
                        ,bg="lime",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        # Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12
                          ,font=("times new roman",13,"bold")
                          ,bg="lime",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5)

        # Delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12
                          ,font=("times new roman",13,"bold")
                          ,bg="lime",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)

        # Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12
                         ,font=("times new roman",13,"bold")
                         ,bg="lime",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)

        # buttons 2 frame
        btn2_frame=Frame(classStudent,bd=2,relief=RIDGE,bg="ghostwhite")
        btn2_frame.place(x=10,y=210,width=565,height=50)

        # Take Photo button
        take_photo_btn=Button(btn2_frame,text="Take Photo Sample",command=self.generate_dataset
                              ,width=54,font=("times new roman",13,"bold")
                              ,bg="crimson",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=5,pady=5)

        # # Update Photo button
        # update_photo_btn=Button(btn2_frame,text="Update Photo Sample"
        #                         ,width=26,font=("times new roman",13,"bold")
        #                         ,bg="crimson",fg="white")
        # update_photo_btn.grid(row=0,column=1,padx=5,pady=5)


        #right label frame
        rightframe=LabelFrame(main_frame,bd=2,bg="wheat",relief=RIDGE
                             ,text="Student details"
                             ,font=("times new roman",15,"bold"))
        rightframe.place(x=630,y=10,width=600,height=470)

        #Search system
        searchframe=LabelFrame(rightframe,bd=2,bg="white",relief=RIDGE
                             ,text="Search System"
                             ,font=("times new roman",12,"bold"))
        searchframe.place(x=5,y=5,width=585,height=80)

        # Phone No.
        search_label=Label(searchframe,text="Search Bar",font=("serif",12,"bold"),bg="wheat",fg="blue")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(searchframe,font=("serif",12),width=12,state="readonly")
        search_combo["values"]=("Select","StudentId","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        search_entry=ttk.Entry(searchframe,width=15,font=("serif",12))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        # Search button
        search_btn=Button(searchframe,text="Search",width=8
                          ,font=("times new roman",13,"bold")
                          ,bg="lime",fg="white")
        search_btn.grid(row=0,column=3,padx=2,pady=5)

        # Show button
        showAll_btn=Button(searchframe,text="Show",width=8
                         ,font=("times new roman",13,"bold")
                         ,bg="lime",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2,pady=5)

        # Table frame
        tableframe=Frame(rightframe,bd=2,bg="white",relief=RIDGE)
        tableframe.place(x=5,y=95,width=585,height=340)

        #Scroll bar
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.student_table=ttk.Treeview(tableframe,columns=("dep","course","year","sem","id"
                                                  ,"name","section","gender","phoneNo","emailId","att_count"),
                                                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phoneNo",text="Phone No")
        self.student_table.heading("emailId",text="Email-Id")
        self.student_table.heading("att_count",text="No. of attendence")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phoneNo",width=100)
        self.student_table.column("emailId",width=100)
        self.student_table.column("att_count",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # *********function declaration **********

    def add_data(self):
        #validation
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:#4 parameters are passed in this 1.host 2.username 3.password 4.database
            self.var_attendence_count.set(0)
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_attendence_count.get()
                ))
                conn.commit()
                conn.close()

                self.generate_dataset()
                self.fetch_data()

                messagebox.showinfo("Successfully","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ========= for fetching data ===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ============== get cursor ============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        # self.var_attendence_count.set(data[10])

    # ============= Update function ================
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Dou you want to update this student details ?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,section=%s,gender=%s,phone_no=%s,email_id=%s where student_id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        # self.var_attendence_count.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # =============== delete data ======
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.reset_data()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully deleted","Student data deleted successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    # =========== reset data =============
    def reset_data(self):
        self.var_dept.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_section.set("Select Section"),
        self.var_gender.set("male"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_attendence_count.set(value=0)

    # ============= generate dataset or take photo samples =============
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:        
                conn=mysql.connector.connect(host="localhost",username="root",password="alok2565,",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,section=%s,gender=%s,phone_no=%s,email_id=%s,att_count=%s where student_id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_attendence_count.get(),
                        self.var_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                #self.update_data()
                self.reset_data()
                conn.close()

                # =========== Load predefined data on face frontals from opencv ===========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #color image to gray scale
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filepath="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filepath,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__=="__main__":
    #We used tk module through root and then passed root into 
    root=Tk()
    obj=Student(root)
    root.mainloop()