from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
import numpy as np
import mysql.connector
import cv2

mydata=[]#csv file se sara data isme lenge

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x650+0+0")
        self.root.title("Attendence window")

        # ============== variables =============
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_att=StringVar()

        title_lbl=Label(self.root,text="Check Attendence"
                        ,font=("times new roman",40,"bold")
                        ,bg="wheat",fg="red",compound="center")
        title_lbl.place(x=0,y=0,width=1280,height=130)

        main_frame=Frame(self.root,bd=2,bg="gainsboro")
        main_frame.place(x=15,y=140,width=1240,height=500)

        #left label frame
        leftframe=LabelFrame(main_frame,bd=2,bg="wheat",relief=RIDGE
                             ,text="Student Attendence details"
                             ,font=("times new roman",20,"bold"))
        leftframe.place(x=10,y=10,width=610,height=470)

        #left_inside_frame=Frame(leftframe,bd=2,bg="wheat",relief=RIDGE)
        #left_inside_frame.place(x=5,y=5,width=600,height=200)

        # student id
        studentId_label=Label(leftframe,text="Student Id :",font=("serif",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        studentId_entry=ttk.Entry(leftframe,textvariable=self.var_atten_id,width=16,font=("serif",12))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        name_label=Label(leftframe,text="Name :",font=("serif",13,"bold"))
        name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        name_entry=ttk.Entry(leftframe,textvariable=self.var_atten_name,width=16,font=("serif",12))
        name_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # Department
        dep_label=Label(leftframe,text="Department :",font=("serif",13,"bold"))
        dep_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        dep_entry=ttk.Entry(leftframe,textvariable=self.var_atten_dep,width=16,font=("serif",12))
        dep_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Attendence
        attendence_label=Label(leftframe,text="Attendence :",font=("serif",13,"bold"))
        attendence_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        #attendence_entry=ttk.Entry(leftframe,width=16,font=("serif",12))
        #attendence_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        attendence_combo=ttk.Combobox(leftframe,textvariable=self.var_atten_att,font=("serif",12),width=14,state="readonly")
        attendence_combo["values"]=("Status","Present","Absent")
        attendence_combo.current(0)
        attendence_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # date
        date_label=Label(leftframe,text="Date :",font=("serif",13,"bold"))
        date_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        date_entry=ttk.Entry(leftframe,textvariable=self.var_atten_date,width=16,font=("serif",12))
        date_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # time
        time_label=Label(leftframe,text="Time :",font=("serif",13,"bold"))
        time_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        time_entry=ttk.Entry(leftframe,textvariable=self.var_atten_time,width=16,font=("serif",12))
        time_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #buttons frame
        btn_frame=Frame(leftframe,bd=2,relief=RIDGE,bg="ghostwhite")
        btn_frame.place(x=8,y=370,width=595,height=50)

        # Import button
        import_btn=Button(btn_frame,text="Import",command=self.importCsv,width=13
                        ,font=("times new roman",13,"bold")
                        ,bg="lime",fg="white")
        import_btn.grid(row=0,column=0,padx=5,pady=5)

        # Export button
        export_btn=Button(btn_frame,text="Export",width=13,command=self.exportCsv
                          ,font=("times new roman",13,"bold")
                          ,bg="lime",fg="white")
        export_btn.grid(row=0,column=1,padx=5,pady=5)

        # update button
        update_btn=Button(btn_frame,text="Update",width=13
                          ,font=("times new roman",13,"bold")
                          ,bg="lime",fg="white")
        update_btn.grid(row=0,column=2,padx=5,pady=5)

        # Reset button
        reset_btn=Button(btn_frame,text="Reset",width=12,command=self.reset_data
                         ,font=("times new roman",13,"bold")
                         ,bg="lime",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)

        #right label frame
        rightframe=LabelFrame(main_frame,bd=2,bg="wheat",relief=RIDGE
                             ,text="Student details"
                             ,font=("times new roman",15,"bold"))
        rightframe.place(x=630,y=10,width=600,height=470)

        table_frame=Frame(rightframe,bd=2,relief=RIDGE,bg="ghostwhite")
        table_frame.place(x=5,y=5,width=585,height=400)

        # ================= Scroll bar table ===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendence_table=ttk.Treeview(table_frame,columns=("stuId","name","dep","Date","Time"
                                                  ,"Attendence"),
                                                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendence_table.xview)
        scroll_y.config(command=self.attendence_table.yview)

        self.attendence_table.heading("stuId",text="Student Id")
        self.attendence_table.heading("name",text="Name")
        self.attendence_table.heading("dep",text="Department")
        self.attendence_table.heading("Date",text="Date")
        self.attendence_table.heading("Time",text="Time")
        self.attendence_table.heading("Attendence",text="Attendence")
        self.attendence_table["show"]="headings"
        
        self.attendence_table.column("stuId",width=100)
        self.attendence_table.column("name",width=120)
        self.attendence_table.column("dep",width=100)
        self.attendence_table.column("Date",width=100)
        self.attendence_table.column("Time",width=100)
        self.attendence_table.column("Attendence",width=100)

        self.attendence_table.pack(fill=BOTH,expand=1)
        self.attendence_table.bind("<ButtonRelease>",self.get_cursor)

    # ========== fetch attendence data ==============
    def fetch_data(self,rows):
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert("",END,values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV"
                                       ,filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found")
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV"
                                       ,filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo("Data exported","Your data exported to "+os.path.basename(fln)+"successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # function when clicked on any tuple then it shows that data into entry fills
    def get_cursor(self,event=""):
        cursor_row=self.attendence_table.focus()
        content=self.attendence_table.item(cursor_row)
        rows=content["values"]

        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_date.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_att.set(rows[5])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_att.set("")
    


if __name__=="__main__":
    #We used tk module through root and then passed root into 
    root=Tk()
    obj=Attendence(root)
    root.mainloop()