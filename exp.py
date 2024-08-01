import DataBaseOperations as T
from tkinter import *
import psycopg2
class DBD:    
    def __init__(self):  
        self.root =Tk()
        self.root.geometry("400x580")
        self.root.config(bg="#a39ea0")
        self.root.title("DataManager")
        self.h=""
        self.p=""
        self.u=""
        self.bdn=""
        
        
        Label(self.root,text="data for database connection:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=10)

        Label(self.root,text="host:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=50)
        self.host=StringVar()
        Entry(self.root, textvariable=self.host,font=('Arial,15,bold')).place(x=10,y=90)

        Label(self.root,text="password:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=150)
        self.password=StringVar()
        Entry(self.root, textvariable=self.password,font=('Arial,15,bold')).place(x=10,y=190)

        Label(self.root,text="user:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=250)
        self.user=StringVar()
        Entry(self.root, textvariable=self.user,font=('Arial,15,bold')).place(x=10,y=290)

        Label(self.root,text="dbname:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=350)
        self.dbname=StringVar()
        Entry(self.root, textvariable=self.dbname,font=('Arial,15,bold')).place(x=10,y=390)

        Button(self.root, text="Enter",font=('Arial,15,bold'),command=self.Enter).place(x=10,y=460)
        Button(self.root, text="Skip",font=('Arial,15,bold'),command=self.Skip).place(x=10,y=500)

        self.root.mainloop()

    def Enter(self):
        self.h=self.host.get()
        self.p=self.password.get()
        self.u=self.user.get()
        self.bdn=self.dbname.get()
        global p1 ; p1= self.h
        global p2 ; p2= self.p
        global p3 ; p3= self.u
        global p4 ; p4= self.bdn
        if T.TryDataBaseConnection(p4 , p3 , p1 , p2 )==True:
            self.root.destroy()

        
    def Skip(self):
        self.h=None
        self.p=None
        self.u=None
        self.bdn=None
        if T.TryDataBaseConnection(None , None , None , None )==True:
            self.root.destroy()


    

DBD()
print(p1 , p2)
