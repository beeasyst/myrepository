
import psutil
import os
import psycopg2
def passage(filename, pathtocurrentdirrectory , mass=None):
    m=os.listdir(pathtocurrentdirrectory)
    for i in m:
        curpath=os.path.normpath(os.path.join(pathtocurrentdirrectory ,i))
        if i==filename:
            if mass==None:
                return curpath
            else:
                mass.append(curpath)
        if os.path.isdir(curpath)!=False:
            try:
                r=passage(filename , curpath , mass)
                if mass==None:
                    if isinstance(r,str):
                        return r
            except WindowsError:
                pass
    return 0
def PSQLstart():
    PSQLf=False
    for proc in psutil.process_iter(): 
        if "postgre" in proc.name():
            PSQLf=True
            print("PSQLf")
            break;
    if not(PSQLf):
        m=list(psutil.disk_partitions())
        for i in m:
            print(i.device)
            if i.fstype=='NTFS':
                mass=[]
                count=0
                t=passage("postgres.exe" , i.device)
                print(t)
                if isinstance(t,str):
                    d=passage("data" , i.device , mass)
                    for j in mass:
                        print(j)
                        if isinstance(passage("base" , j) , str):
                            print(t+" -D "+j)
                            os.system(t+" -D "+j)
                            for proc in psutil.process_iter(): 
                                if "postgre" in proc.name():
                                    PSQLf=True

                                    print("connection succesful")
                            break
                        else:
                            print("uncorrect path")
                    if PSQLf==True:
                        break
                else:
                    print("connection failed")
def TryDataBaseConnection(bdn , u , h , p):
    p1= "postgres"
    p2= "postgres"
    p3= "127.0.0.1"
    p4= "qwerty"
    if bdn!="" and bdn!=None: p1= bdn
    if u!="" and u!=None: p2=u
    if h!="" and h!=None: p3= h
    if p!="" and p!=None: p4= p
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=p1, user=p2, password=p4, host=p3)
        print('succesful connection') 
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return False
    else:
        return True

        

class DBC:
    def 

def AA(login , password):
    datacor=False

    if datacor==True:
        return 0;
    if datacor==False:
        return 1;
def CA(login , password):
    prres=False

    if prres==True:
        return 0;
    if prres==False:
        return 1;
