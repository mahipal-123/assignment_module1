import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists Biling_Database")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="Billing_Database")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists cosmetic_items(id int primary key auto_increment ,Bath_Soap int(12),Face_Cream int(12),Face_Wash int(12),Hair_Spray int(12),Total int(12))")
mydb.commit()
