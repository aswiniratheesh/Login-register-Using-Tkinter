from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Python:Simple Inventory System")
import mysql
USERNAME=StringVar()
PASSWORD=StringVar()
FIRSTNAME=StringVar()
LASTNAME=StringVar()

def db():
    global mydb,mycursor
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase")
    mycursor=mydb.cursor()
    
def Exit():
    result=tkMessageBox.askquestion('System','Are You Sure You Want To Exit?',icon="warning")
    if(result=='yes'):
       root.destroy()
       exit()
       
def LoginForm():
    global LoginFrame,lbl_result1
    
    LoginFrame=Frame(root)
    LoginFrame.pack(side=TOP,pady=80)
    
    lbl_username=Label(LoginFrame, text="Username:",font=('arial',25), bd=18)
    lbl_username.grid(row=1)
    
    lbl_password=Label(LoginFrame,text="Password",font=('areal',25), bd=18)
    lbl_password.grid(row=2)
    
    lbl_result1=Label(LoginFrame,text="",font=('areal',18))
    lbl_result1.grid(row=3,columnspan=2)

    username=Entry(LoginFrame,font=('areal',20),textvariable=USERNAME,width=15)
    username.grid(row=1,column=1)

    password=Entry(LoginFrame,font=('areal',20),textvariable=PASSWORD,width=15,show="*")
    password.grid(row=2,column=1)

    btn_login=Button(LoginFrame,text="Login",font=('areal',18),width=35,command=Login)
    btn_login.grid(row=4,columnspan=2,pady=20)

    lbl_register=Label(LoginFrame, text="Register", fg="Blue",font=('arial',12))
    lbl_register.grid(row=0,stick=W)
    lbl_register.bind('<Button-1>',ToggleToRegister)
def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()



def RegisterForm():
    global RegisterFrame,lbl_result2
    
    RegisterFrame=Frame(root)
    RegisterFrame.pack(side=TOP,pady=40)
    
    lbl_username=Label(RegisterFrame, text="Username:",font=('arial',18), bd=30)
    lbl_username.grid(row=1)
    
    lbl_password=Label(RegisterFrame,text="Password",font=('areal',18), bd=18)
    lbl_password.grid(row=2)

    lbl_firstname=Label(RegisterFrame,text="Firstname",font=('areal',18), bd=18)
    lbl_firstname.grid(row=3)

    lbl_lastname=Label(RegisterFrame,text="Lastname",font=('areal',18), bd=18)
    lbl_lastname.grid(row=4)
        
    
    lbl_result2=Label(RegisterFrame,text="",font=('areal',18))
    lbl_result2.grid(row=5,columnspan=2)

    username=Entry(RegisterFrame,font=('areal',20),textvariable=USERNAME,width=15)
    username.grid(row=1,column=1)

    password=Entry(RegisterFrame,font=('areal',20),textvariable=PASSWORD,width=15,show="*")
    password.grid(row=2,column=1)

    firstname=Entry(RegisterFrame,font=('areal',20),textvariable=FIRSTNAME,width=15)
    firstname.grid(row=3,column=1)

    lastname=Entry(RegisterFrame,font=('areal',20),textvariable=LASTNAME,width=15)
    lastname.grid(row=4,column=1)
    

    btn_login=Button(RegisterFrame,text="Register",font=('areal',18),width=35,command=Register)
    btn_login.grid(row=6,columnspan=2,pady=20)

    lbl_login=Label(RegisterFrame, text="Login", fg="Blue",font=('arial',12))
    lbl_login.grid(row=0,stick=W)
    lbl_login.bind('<Button-1>',ToggleToLogin)
    


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()
    
def Register():
    db()
    uname=USERNAME.get()
    pas=PASSWORD.get()
    fi=FIRSTNAME.get()
    li=LASTNAME.get()
    if uname=="" or pas=="" or fi=="" or li=="":
        lbl_result2.config(text="Please complete the required field",fg="orange")
    else:
        sql="SELECT *FROM tklogreg where USERNAME=%s"
        val=(uname,)
        mycursor.execute(sql,val)
        if mycursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken",fg="red")
        else:
            sql="INSERT INTO tklogreg(USERNAME,PASSWORD,FIRSTNAME,LASTNAME)values(%s,%s,%s,%s)"
            val=(uname,pas,fi,li)
            mycursor.execute(sql,val)
            mydb.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!",fg="green")
        mycursor.close()
        mydb.close()

def Login():
    db()
    uname=USERNAME.get()
    pas=PASSWORD.get()

    if uname=="" or pas=="":
        lbl_result1.config(text="Please complete the required field",fg="orange")
    else:
        sql="SELECT *FROM tklogreg where USERNAME=%s and PASSWORD=%s"
        val=(uname,pas)
        mycursor.execute(sql,val)
        if mycursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login.",fg="green")
            
            USERNAME.set("")
            PASSWORD.set("")
        else:
            
           
            lbl_result1.config(text="Invalid username or password.",fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        mycursor.close()
        mydb.close()
LoginForm()
    


