from tkinter import *
import DataBaseOperations as DBO
from tkinter import *
class DBD:    
    def __init__(self):  
        self.root =Tk()
        self.root.geometry("400x580")
        self.root.config(bg="#a39ea0")
        self.root.title("DataManager")
        
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
        hc=self.host.get()
        pc=self.password.get()
        uc=self.user.get()
        bdnc=self.dbname.get()
        self.root.destroy()
        return bdnc , uc , hc , pc
        
        
    def Skip(self):
        self.root.destroy()
        return None  , None , None , None

class Error:
    def __init__ (self , massage):
        wind=Tk()
        wind.geometry("300x200")
        wind.config(bg="#a39ea0")
        wind.title("Error")

        Label(wind,text= massage, font=('Arial,10,bold'),bg='#a39ea0').pack(expand = True)
        wind.mainloop()
class AutorizationPage:

    def __init__(self):
        self.bre=False;
        self.root =Tk()
        self.root.geometry("400x500")
        self.root.config(bg="#a39ea0")
        self.root.title("DataManager")

        Label(self.root,text="Login:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=10)
        self.elogin=StringVar()
        Entry(self.root, textvariable=self.elogin,font=('Arial,15,bold')).place(x=10,y=50)

        Label(self.root,text="Password:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=110)
        self.epassw=StringVar()
        Entry(self.root, textvariable=self.epassw,font=('Arial,15,bold')).place(x=10,y=150)

        Button(self.root, text="Enter",font=('Arial,15,bold'),command=self.Enter).place(x=10,y=240)
        Button(self.root, text="Create account",font=('Arial,15,bold'),command=self.CreateAccount ).place(x=10,y=340)
        
        
        
        self.root.mainloop()

    def Enter(self):
        l=self.elogin.get()
        p=self.epassw.get()
        self.bre=DBO.AA(l , p);
        if not(self.bre):
                Error("Autorization Failure")


    def CreateAccount(self):
        self.root.destroy()
        self.bre=True
        RegistrationPage()

class RegistrationPage:

    def __init__ (self):
        self.bre=False
        self.root=Tk()
        self.root.geometry("400x700")
        self.root.config(bg="#a39ea0")
        self.root.title("DataManager")

        Label(self.root,text="Username:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=10)
        self.eusname=StringVar()
        Entry(self.root, textvariable=self.eusname,font=('Arial,15,bold')).place(x=10,y=50)

        Label(self.root,text="Password:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=110)
        self.epassw=StringVar()
        Entry(self.root, textvariable=self.epassw,font=('Arial,15,bold')).place(x=10,y=150)

        Label(self.root,text="Password again:", font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=210)
        self.epasswa=StringVar()
        Entry(self.root, textvariable=self.epasswa,font=('Arial,15,bold')).place(x=10,y=250)

        Button(self.root, text="Create",font=('Arial,15,bold'),command=self.Create).place(x=10,y=310)
        Button(self.root, text="Back",font=('Arial,15,bold'),command=self.Back).place(x=10,y=370)
        if self.bre==True:
            (self.root.destoy())
        self.root.mainloop()

    def Back(self):
        self.root.destroy()
        AutorizationPage()
        return 0;

    def Create(self):
        if self.eusname.get()!='' and self.epassw.get()!='' and self.epasswa.get()!='':
            l=self.eusname.get()
            p1=self.epassw.get()
            p2=self.epasswa.get()
            if l!='' or p1!='' or p2!='':
                Error("Uncorrect data")
                
                if p1==p2:
                    self.bre=DBO.CA(l , p1)
                    if not(self.bre):
                        Error("Creation Failure")
                        
                else:
                    Error("Passwords are not similar")
                    self.epassw.clear()
                    self.epasswa.clear()
            
        else:
            Error("Uncorrect data")
            return self.bre;