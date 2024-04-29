import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists Billing_Database")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="Billing_Database")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists software(id int primary key auto_increment ,Customer_name varchar(30),Phone_no Bigint(12),Bill_no int(12))")
mydb.commit()
