import mysql.connector
from tkinter import messagebox


def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb =  mysql.connector.connect(host='LAPTOP-4NP0IFT9',user='root@localhost',password="Chandana@2004")
        mycursor=mydb.cursor()
        print("Connection stablished")
    except:
        messagebox.showerror("Connection","Database connection not stablished!!")
    try:
       command="create database Heartattack_Data"
       mycursor.execute(command)

       command="use Heartattack_Data"
       mycursor.execute(command)

       command="create table data(user int auto_increment key not null, Name varchar(50),Date varchar(50), DOB varchar(100), age varchar(100), sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), restecg varchar(100), thalach varchar(100), oldpeak varchar(100), slop varchar(100), ca varchar(100), thal varchar(100), result varchar(100))"
       mycursor.execute(command)

       command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalch,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       mycursor.execute(command)
       mydb.commit()
       mydb.close()
       messagebox.showinfo("Register","New user added sucessfully!!!!")


    except:
        pass


        
        



    



    


Save_Data_MySql()
