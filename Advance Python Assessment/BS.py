from tkinter import *
from BS_Data1 import *
from tkinter import messagebox
import pymysql
import random

bill_no=random.randint(500,1000)  # take random value
root=Tk()
def enter():
    #id=e_id.get()
    Customer_name=c_name.get()
    Phone_no=p_no.get()
    Bill_no=b_no.get()

    query="insert into software(Customer_name,Phone_no,Bill_no) values('%s','%s','%s')"
    args=(Customer_name,Phone_no,Bill_no)
    mycursor.execute(query%args)
    mydb.commit()

"""def Insert():
    #id=e_id.get()
    Bath_Soap=b_shop.get()
    Face_Cream=f_cream.get()
    Face_Wash=f_wash.get()
    Hair_Spray=h_spray.get()
    total_comestic=t_cosmetic.get()

    query="insert into cosmetic_items(Bath_Soap,Face_Cream,Face_Wash,Hair_Spray,total_cosmetic) values('%s','%s','%s','%s','%s')"
    args=(Bath_Soap,Face_Cream,Face_Wash,Hair_Spray,total_comestic)
    mycursor.execute(query%args)
    mydb.commit()"""

def add():
    global Bath_Soap,Face_Cream,Face_Wash,Hair_Spray,Food_Oil,Rice,Daal,Wheat,Sugar,Maza,Coke,Frooti,Nimkos,Biscutes
    global total # global variable use to store bill value  in text area
    Bath_Soap = int(b_shop.get())*20 # get () function fetch value ex to calculate default price 
    Face_Cream = int(f_cream.get())*40
    Face_Wash  = int(f_wash.get())*70
    Hair_Spray = int(h_spray.get())*50
    Food_Oil   = int(food_oil.get())*48
    Rice       = int(rice.get())*35
    Daal       = int(daal.get())*35
    Wheat      = int(wheat.get())*35
    Sugar      = int(sugar.get())*35
    Maza       = int(maza.get())*48
    Coke       = int(coke.get())*35
    Frooti     = int(frooti.get())*35
    Nimkos     = int(nimkos.get())*35
    Biscutes   = int(biscutes.get())*35
    
    result = Bath_Soap + Face_Cream + Face_Wash + Hair_Spray 
    result1 = Food_Oil + Rice + Daal + Wheat + Sugar
    result2 = Maza + Coke + Frooti + Nimkos + Biscutes
    tax1=result * 0.12
    tax2=result1 * 0.05
    tax3=result2 * 0.08

# insert method use ti nisert value in entry box

    cosmetic_t.insert(0,int(tax1))
    grocery_t.insert(0,int(tax2))
    Other_t.insert(0,int(tax3))
    t_cosmetic.insert(0,int(result))
    t_grocery.insert(0,int(result1))
    other.insert(0,int(result2))

    total=result + result1 + result2 + tax1 + tax2 +tax3
 
 # delete method use to delete all bill value 
def delete(): 
    t_cosmetic.delete(0)   # And 0 use to delete bill balue because without define 0 it is not calculate the price and show null error 
    t_grocery.delete(0)
    other.delete(0)          
    cosmetic_t.delete(0)
    grocery_t.delete(0)
    Other_t.delete(0)
    b_shop.delete(0)
    f_cream.delete(0)
    f_wash.delete(0)
    h_spray.delete(0)
    food_oil.delete(0)
    rice.delete(0)
    daal.delete(0)
    wheat.delete(0)
    sugar.delete(0)
    maza.delete(0)
    coke.delete(0)
    frooti.delete(0)
    nimkos.delete(0)
    biscutes.delete(0)

    """b_shop.insert(0)
    f_cream.insert(0)
    f_wash.insert(0)
    h_spray.insert(0)
    food_oil.insert(0)
    rice.insert(0)
    daal.insert(0)
    wheat.insert(0)
    sugar.insert(0)
    maza.insert(0)
    coke.insert(0)
    frooti.insert(0)
    nimkos.insert(0)
    biscutes.insert(0)"""
   

def BillArea(): 
            if c_name.get()=='' and p_no.get()=='':
                messagebox.showerror("Error" ,"Please enter Customer Details")
            elif t_cosmetic.get()=='' or t_grocery.get()=='' or other.get()=='':
                messagebox.showerror("Error" , "Please enter Prdduct Details")
            else:

             textarea.insert(END,'\t*** Welcometo customer retail***\n')
             textarea.insert(END,f'Bill No :{bill_no}\n')  # use random function 
             textarea.insert(END,f'Customer Name :{c_name.get()}\n')
             textarea.insert(END,f'Phone Num :{p_no.get()}\n')
             textarea.insert(END,'==================================================\n')
             textarea.insert(END,'Prodcut\t\t\tQty\t\tPrice\n')
             textarea.insert(END,'==================================================\n')

             

             if b_shop.get()!='0':
                 textarea.insert(END,f'Bath Soap\t\t\t{b_shop.get()}\t\t{Bath_Soap}\n')
             if f_cream.get()!='0':
                textarea.insert(END,f'Face Cream\t\t\t{f_cream.get()}\t\t{Face_Cream}\n')
             if f_wash.get()!='0':
                textarea.insert(END,f'Face Wash\t\t\t{f_wash.get()}\t\t{Face_Wash}\n')

             if h_spray.get()!='0':
                textarea.insert(END,f'Hair Spray\t\t\t{h_spray.get()}\t\t{Hair_Spray}\n')

             if food_oil.get()!='0':
                 textarea.insert(END,f'Food Oil\t\t\t{food_oil.get()}\t\t{Food_Oil}\n')
             if daal.get()!='0':
                textarea.insert(END,f'Daal\t\t\t{daal.get()}\t\t{Daal}\n')
             if rice.get()!='0':
                 textarea.insert(END,f'Rice\t\t\t{rice.get()}\t\t{Rice}\n')
             if sugar.get()!='0':
                textarea.insert(END,f'Sugar\t\t\t{sugar.get()}\t\t{Sugar}\n')
             if frooti.get()!='0':
                textarea.insert(END,f'Frooti\t\t\t{frooti.get()}\t\t{Frooti}\n')
             if coke.get()!='0':
                textarea.insert(END,f'Cock\t\t\t{coke.get()}\t\t{Coke}\n')
             if nimkos.get()!='0':
                textarea.insert(END,f'Nimkos\t\t\t{nimkos.get()}\t\t{Nimkos}\n')
             if maza.get()!='0':
                textarea.insert(END,f'Maza\t\t\t{maza.get()}\t\t{Maza}\n')
             if biscutes.get()!='0':
                 textarea.insert(END,f'Biscuties\t\t\t{biscutes.get()}\t\t{Biscutes}\n')
             if wheat.get()!='0':
                textarea.insert(END,f'Wheat\t\t\t{wheat.get()}\t\t{Wheat}\n')
             
             textarea.insert(END,'==================================================\n')

             if cosmetic_t.get()!='0':
                 textarea.insert(END,f'Cosmetic Tax\t\t\t{cosmetic_t.get()}\n')
             if grocery_t.get()!='0':
                 textarea.insert(END,f'Grocery Tax\t\t\t{grocery_t.get()}\n')
             if Other_t.get()!='0':
                 textarea.insert(END,f'Other Tax\t\t\t{Other_t.get()}\n')

             textarea.insert(END,'==================================================\n')
             
           
             textarea.insert(END,f'Total Bill:{total}\n')

def exit():
    root.destroy() # destroy method use to terminate gui

root.geometry("4000x1000")
root.title(" Software ")
root['background']='#856ff8'
Billing_Software=Label(root,font=("Arial",20,"bold"),text="Billing_Software")
Billing_Software.pack()
Customer_Details=Label(root,font=("Arial",10,"bold"),text="Customer Details",fg="red",width=40)
Customer_Details.place(x=1,y=100)
Customer_name=Label(root,font=("Arial",10,"bold"),text="Customer Name")
Customer_name.place(x=10,y=150)
c_name=Entry(root,bg="White",width=30,)
c_name.place(x=150,y=150)

Phone_no=Label(root,font=("Arial",10,"bold"),text="Phone no")
Phone_no.place(x=350,y=150)
p_no=Entry(root,bg="White",width=30,)
p_no.place(x=450,y=150)

Bill_no=Label(root,font=("Arial",10,"bold"),text="Bill no")
Bill_no.place(x=650,y=150)
b_no=Entry(root,bg="White",width=10,)
b_no.place(x=720,y=150)

Enter=Button(root,font=("Arial",10,"bold"),text="Enter",fg="Black",command=enter)
Enter.place(x=850,y=150) 

Cosmetics=Label(root,font=("Arial",10,"bold"),text="Cosmetics",fg="red",width=20)
Cosmetics.place(x=1,y=200)

Grocery=Label(root,font=("Arial",10,"bold"),text="Grocery",fg="red",width=20)
Grocery.place(x=300,y=200)

Other=Label(root,font=("Arial",10,"bold"),text="Other",fg="red",width=20)
Other.place(x=600,y=200)

Bath_Soap=Label(root,font=("Arial",10,"bold"),text="Bath Soap")
Bath_Soap.place(x=1,y=240)
b_shop=Entry(root,bg="White",width=15)
b_shop.place(x=95,y=240)
b_shop.insert(0,0)

Rice=Label(root,font=("Arial",10,"bold"),text="Rice")
Rice.place(x=300,y=240)
rice=Entry(root,bg="White",width=15)
rice.place(x=380,y=240)
rice.insert(0,0)

Maza=Label(root,font=("Arial",10,"bold"),text="Maza")
Maza.place(x=600,y=240)
maza=Entry(root,bg="White",width=15)
maza.place(x=665,y=240)
maza.insert(0,0)

Coke=Label(root,font=("Arial",10,"bold"),text="Coke")
Coke.place(x=600,y=280)
coke=Entry(root,bg="White",width=15)
coke.place(x=665,y=280)
coke.insert(0,0)

Frooti=Label(root,font=("Arial",10,"bold"),text="Frooti")
Frooti.place(x=600,y=320)
frooti=Entry(root,bg="White",width=15)
frooti.place(x=665,y=320)
frooti.insert(0,0)

Nimkos=Label(root,font=("Arial",10,"bold"),text="Nimkos")
Nimkos.place(x=600,y=360)
nimkos=Entry(root,bg="White",width=15)
nimkos.place(x=665,y=360)
nimkos.insert(0,0)

Biscutes=Label(root,font=("Arial",10,"bold"),text="Biscutes")
Biscutes.place(x=600,y=400)
biscutes=Entry(root,bg="White",width=15)
biscutes.place(x=665,y=400)
biscutes.insert(0,0)

Face_Cream=Label(root,font=("Arial",10,"bold"),text="Face Cream")
Face_Cream.place(x=1,y=280)
f_cream=Entry(root,bg="White",width=15,)
f_cream.place(x=95,y=280)
f_cream.insert(0,0)

Food_Oil=Label(root,font=("Arial",10,"bold"),text="Food Oil")
Food_Oil.place(x=300,y=280)
food_oil=Entry(root,bg="White",width=15)
food_oil.place(x=380,y=280)
food_oil.insert(0,0)

Face_Wash=Label(root,font=("Arial",10,"bold"),text="Face Wash")
Face_Wash.place(x=1,y=320)
f_wash=Entry(root,bg="White",width=15,)
f_wash.place(x=95,y=320)
f_wash.insert(0,0)

Daal=Label(root,font=("Arial",10,"bold"),text="Daal")
Daal.place(x=300,y=320)
daal=Entry(root,bg="White",width=15)
daal.place(x=380,y=320)
daal.insert(0,0)

Wheat=Label(root,font=("Arial",10,"bold"),text="Wheat")
Wheat.place(x=300,y=360)
wheat=Entry(root,bg="White",width=15)
wheat.place(x=380,y=360)
wheat.insert(0,0)

Sugar=Label(root,font=("Arial",10,"bold"),text="Sugar")
Sugar.place(x=300,y=400)
sugar=Entry(root,bg="White",width=15)
sugar.place(x=380,y=400)
sugar.insert(0,0)

Hair_Spray=Label(root,font=("Arial",10,"bold"),text="Hair Spray")
Hair_Spray.place(x=1,y=360)
h_spray=Entry(root,bg="White",width=15,)
h_spray.place(x=95,y=360)
h_spray.insert(0,0)



#insert=Button(root,font=("Arial",16,"bold"),text="Insert",fg="Red",command=Insert)
#insert.place(x=1,y=400) 

total_comestic=Label(root,font=("Arial",10,"bold"),text="Total Cosmetic")
total_comestic.place(x=1,y=450)
t_cosmetic=Entry(root,bg="White",width=15,)
t_cosmetic.place(x=125,y=450)

total_grocery=Label(root,font=("Arial",10,"bold"),text="Total Grocery")
total_grocery.place(x=1,y=500)
t_grocery=Entry(root,bg="White",width=15)
t_grocery.place(x=125,y=500)

Other_total=Label(root,font=("Arial",10,"bold"),text="Other Total")
Other_total.place(x=1,y=550)
other=Entry(root,bg="White",width=15)
other.place(x=125,y=550)

Cosmetic_Price=Label(root,font=("Arial",10,"bold"),text="Cosmetic Tax")
Cosmetic_Price.place(x=295,y=450)
cosmetic_t=Entry(root,bg="White",width=15,)
cosmetic_t.place(x=400,y=450)

Grocery_tax=Label(root,font=("Arial",10,"bold"),text="Grocery Tax")
Grocery_tax.place(x=295,y=490)
grocery_t=Entry(root,bg="White",width=15,)
grocery_t.place(x=400,y=490)

Other_tax=Label(root,font=("Arial",10,"bold"),text="Other Tax")
Other_tax.place(x=295,y=530)
Other_t=Entry(root,bg="White",width=15,)
Other_t.place(x=400,y=530)

billframe=Frame(root)   # billframe use to set text area in particular 
billframe.place(x=800,y=200)

bill=Label(billframe,font=("Arial",10,"bold"),text="Bill Area")
bill.pack()


textarea=Text(billframe,height=20,width=50)
textarea.pack() # In textarea to print all bill value


add_button = Button(root, font=("Arial",16,"bold"),text="Total",fg="Red", command=add)
add_button.place(x=550,y=450)

Delete = Button(root, font=("Arial",16,"bold"),text="Delete",fg="Red",command=delete)
Delete.place(x=550,y=500)

Bill = Button(root, font=("Arial",16,"bold"),text="Bill",fg="Red",command=BillArea) 
Bill.place(x=550,y=550)

Exit = Button(root, font=("Arial",16,"bold"),text="Exit",fg="Red",command=exit)
Exit.place(x=550,y=600)

root.mainloop()# to generate gui