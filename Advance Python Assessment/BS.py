from tkinter import *
import pymysql
import random

# Randomly generate a bill number between 500 and 1000
bill_no = random.randint(500, 1000)

# Initialize the main window
root = Tk()

def enter():
    # Fetch input data
    Customer_name = c_name.get()
    Phone_no = p_no.get()
    Bill_no = b_no.get()

    # Insert the customer data into the database
    query = "insert into software(Customer_name,Phone_no,Bill_no) values('%s','%s','%s')"
    args = (Customer_name, Phone_no, Bill_no)
    mycursor.execute(query % args)
    mydb.commit()

def add():
    global Bath_Soap, Face_Cream, Face_Wash, Hair_Spray, Food_Oil, Rice, Daal, Wheat, Sugar, Maza, Coke, Frooti, Nimkos, Biscutes
    global total

    # Fetch input quantities and calculate item costs
    Bath_Soap = int(b_shop.get()) * 20
    Face_Cream = int(f_cream.get()) * 40
    Face_Wash = int(f_wash.get()) * 70
    Hair_Spray = int(h_spray.get()) * 50
    Food_Oil = int(food_oil.get()) * 48
    Rice = int(rice.get()) * 35
    Daal = int(daal.get()) * 35
    Wheat = int(wheat.get()) * 35
    Sugar = int(sugar.get()) * 35
    Maza = int(maza.get()) * 48
    Coke = int(coke.get()) * 35
    Frooti = int(frooti.get()) * 35
    Nimkos = int(nimkos.get()) * 35
    Biscutes = int(biscutes.get()) * 35

    # Calculate subtotal and taxes for each category
    result = Bath_Soap + Face_Cream + Face_Wash + Hair_Spray
    result1 = Food_Oil + Rice + Daal + Wheat + Sugar
    result2 = Maza + Coke + Frooti + Nimkos + Biscutes
    tax1 = result * 0.12
    tax2 = result1 * 0.05
    tax3 = result2 * 0.08

    # Insert calculated values into the entry widgets
    cosmetic_t.insert(0, int(tax1))
    grocery_t.insert(0, int(tax2))
    Other_t.insert(0, int(tax3))
    t_cosmetic.insert(0, int(result))
    t_grocery.insert(0, int(result1))
    other.insert(0, int(result2))

    # Calculate total bill
    total = result + result1 + result2 + tax1 + tax2 + tax3

def delete():
    # Clear all entry widgets
    t_cosmetic.delete(0)
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

def BillArea():
    if c_name.get() == '' and p_no.get() == '':
        messagebox.showerror("Error", "Please enter Customer Details")
    elif t_cosmetic.get() == '' or t_grocery.get() == '' or other.get() == '':
        messagebox.showerror("Error", "Please enter Product Details")
    else:
        # Print bill details in the textarea
        textarea.insert(END, '\t*** Welcome to Customer Retail ***\n')
        textarea.insert(END, f'Bill No :{bill_no}\n')
        textarea.insert(END, f'Customer Name :{c_name.get()}\n')
        textarea.insert(END, f'Phone Num :{p_no.get()}\n')
        textarea.insert(END, '==================================================\n')
        textarea.insert(END, 'Product\t\t\tQty\t\tPrice\n')
        textarea.insert(END, '==================================================\n')

        # Print item details
        if b_shop.get() != '0':
            textarea.insert(END, f'Bath Soap\t\t\t{b_shop.get()}\t\t{Bath_Soap}\n')
        if f_cream.get() != '0':
            textarea.insert(END, f'Face Cream\t\t\t{f_cream.get()}\t\t{Face_Cream}\n')
        if f_wash.get() != '0':
            textarea.insert(END, f'Face Wash\t\t\t{f_wash.get()}\t\t{Face_Wash}\n')
        if h_spray.get() != '0':
            textarea.insert(END, f'Hair Spray\t\t\t{h_spray.get()}\t\t{Hair_Spray}\n')
        if food_oil.get() != '0':
            textarea.insert(END, f'Food Oil\t\t\t{food_oil.get()}\t\t{Food_Oil}\n')
        if daal.get() != '0':
            textarea.insert(END, f'Daal\t\t\t{daal.get()}\t\t{Daal}\n')
        if rice.get() != '0':
            textarea.insert(END, f'Rice\t\t\t{rice.get()}\t\t{Rice}\n')
        if sugar.get() != '0':
            textarea.insert(END, f'Sugar\t\t\t{sugar.get()}\t\t{Sugar}\n')
        if frooti.get() != '0':
            textarea.insert(END, f'Frooti\t\t\t{frooti.get()}\t\t{Frooti}\n')
        if coke.get() != '0':
            textarea.insert(END, f'Coke\t\t\t{coke.get()}\t\t{Coke}\n')
        if nimkos.get() != '0':
            textarea.insert(END, f'Nimkos\t\t\t{nimkos.get()}\t\t{Nimkos}\n')
        if maza.get() != '0':
            textarea.insert(END, f'Maza\t\t\t{maza.get()}\t\t{Maza}\n')
        if biscutes.get() != '0':
            textarea.insert(END, f'Biscutes\t\t\t{biscutes.get()}\t\t{Biscutes}\n')
        if wheat.get() != '0':
            textarea.insert(END, f'Wheat\t\t\t{wheat.get()}\t\t{Wheat}\n')

        textarea.insert(END, '==================================================\n')

        # Print tax details
        if cosmetic_t.get() != '0':
            textarea.insert(END, f'Cosmetic Tax\t\t\t{cosmetic_t.get()}\n')
        if grocery_t.get() != '0':
            textarea.insert(END, f'Grocery Tax\t\t\t{grocery_t.get()}\n')
        if Other_t.get() != '0':
            textarea.insert(END, f'Other Tax\t\t\t{Other_t.get()}\n')

        textarea.insert(END, '==================================================\n')
        textarea.insert(END, f'Total Bill: {total}\n')

def exit():
    root.destroy()  # Terminate the GUI

# Set window properties
root.geometry("4000x1000")
root.title("Software")
root['background'] = '#856ff8'

# Create and place labels and entry widgets
Billing_Software = Label(root, font=("Arial", 20, "bold"), text="Billing_Software")
Billing_Software.pack()

Customer_Details = Label(root, font=("Arial", 10, "bold"), text="Customer Details", fg="red", width=40)
Customer_Details.place(x=1, y=100)

Customer_name = Label(root, font=("Arial", 10, "bold"), text="Customer Name")
Customer_name.place(x=10, y=150)
c_name = Entry(root, bg="White", width=30)
c_name.place(x=150, y=150)

Phone_no = Label(root, font=("Arial", 10, "bold"), text="Phone no")
Phone_no.place(x=350, y=150)
p_no = Entry(root, bg="White", width=30)
p_no.place(x=450, y=150)

Bill_no = Label(root, font=("Arial", 10, "bold"), text="Bill no")
Bill_no.place(x=650, y=150)
b_no = Entry(root, bg="White", width=10)
b_no.place(x=720, y=150)

Enter = Button(root, font=("Arial", 10, "bold"), text="Enter", fg="Black", command=enter)
Enter.place(x=850, y=150)

Cosmetics = Label(root, font=("Arial", 10, "bold"), text="Cosmetics", fg="red", width=20)
Cosmetics.place(x=1, y=200)

Grocery = Label(root, font=("Arial", 10, "bold"), text="Grocery", fg="red", width=20)
Grocery.place(x=350, y=200)

Other = Label(root, font=("Arial", 10, "bold"), text="Other", fg="red", width=20)
Other.place(x=650, y=200)

# Cosmetics section
Bath_Shop = Label(root, font=("Arial", 10, "bold"), text="Bath Shop")
Bath_Shop.place(x=1, y=250)
b_shop = Entry(root, bg="White", width=20)
b_shop.place(x=120, y=250)

Face_Cream = Label(root, font=("Arial", 10, "bold"), text="Face Cream")
Face_Cream.place(x=1, y=300)
f_cream = Entry(root, bg="White", width=20)
f_cream.place(x=120, y=300)

Face_Wash = Label(root, font=("Arial", 10, "bold"), text="Face Wash")
Face_Wash.place(x=1, y=350)
f_wash = Entry(root, bg="White", width=20)
f_wash.place(x=120, y=350)

Hair_Spray = Label(root, font=("Arial", 10, "bold"), text="Hair Spray")
Hair_Spray.place(x=1, y=400)
h_spray = Entry(root, bg="White", width=20)
h_spray.place(x=120, y=400)

t_cosmetic = Entry(root, bg="White", width=20)
t_cosmetic.place(x=150, y=500)

cosmetic_t = Entry(root, bg="White", width=20)
cosmetic_t.place(x=150, y=550)

# Grocery section
Food_Oil = Label(root, font=("Arial", 10, "bold"), text="Food Oil")
Food_Oil.place(x=350, y=250)
food_oil = Entry(root, bg="White", width=20)
food_oil.place(x=450, y=250)

Rice = Label(root, font=("Arial", 10, "bold"), text="Rice")
Rice.place(x=350, y=300)
rice = Entry(root, bg="White", width=20)
rice.place(x=450, y=300)

Daal = Label(root, font=("Arial", 10, "bold"), text="Daal")
Daal.place(x=350, y=350)
daal = Entry(root, bg="White", width=20)
daal.place(x=450, y=350)

Wheat = Label(root, font=("Arial", 10, "bold"), text="Wheat")
Wheat.place(x=350, y=400)
wheat = Entry(root, bg="White", width=20)
wheat.place(x=450, y=400)

Sugar = Label(root, font=("Arial", 10, "bold"), text="Sugar")
Sugar.place(x=350, y=450)
sugar = Entry(root, bg="White", width=20)
sugar.place(x=450, y=450)

t_grocery = Entry(root, bg="White", width=20)
t_grocery.place(x=500, y=500)

grocery_t = Entry(root, bg="White", width=20)
grocery_t.place(x=500, y=550)

# Other section
Maza = Label(root, font=("Arial", 10, "bold"), text="Maza")
Maza.place(x=650, y=250)
maza = Entry(root, bg="White", width=20)
maza.place(x=750, y=250)

Coke = Label(root, font=("Arial", 10, "bold"), text="Coke")
Coke.place(x=650, y=300)
coke = Entry(root, bg="White", width=20)
coke.place(x=750, y=300)

Frooti = Label(root, font=("Arial", 10, "bold"), text="Frooti")
Frooti.place(x=650, y=350)
frooti = Entry(root, bg="White", width=20)
frooti.place(x=750, y=350)

Nimkos = Label(root, font=("Arial", 10, "bold"), text="Nimkos")
Nimkos.place(x=650, y=400)
nimkos = Entry(root, bg="White", width=20)
nimkos.place(x=750, y=400)

Biscutes = Label(root, font=("Arial", 10, "bold"), text="Biscutes")
Biscutes.place(x=650, y=450)
biscutes = Entry(root, bg="White", width=20)
biscutes.place(x=750, y=450)

other = Entry(root, bg="White", width=20)
other.place(x=800, y=500)

Other_t = Entry(root, bg="White", width=20)
Other_t.place(x=800, y=550)

# Control buttons
Add = Button(root, font=("Arial", 10, "bold"), text="Add", fg="Black", command=add)
Add.place(x=10, y=600)

Delete = Button(root, font=("Arial", 10, "bold"), text="Delete", fg="Black", command=delete)
Delete.place(x=60, y=600)

Bill = Button(root, font=("Arial", 10, "bold"), text="Bill", fg="Black", command=BillArea)
Bill.place(x=120, y=600)

Exit = Button(root, font=("Arial", 10, "bold"), text="Exit", fg="Black", command=exit)
Exit.place(x=200, y=600)

# Text area to display the bill
textarea = Text(root, font=("Arial", 10, "bold"), bg="White", height=20, width=50)
textarea.place(x=900, y=150)

# Database connection
# mydb = pymysql.connect(host="localhost", user="root", password="admin", database="billing")
# mycursor = mydb.cursor()

# Start the Tkinter event loop
root.mainloop()
