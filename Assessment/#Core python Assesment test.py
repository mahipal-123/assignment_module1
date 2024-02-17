#Core python Assesment test
status = True

while status:
    print('''---------------------Welcome to Python E-Note---------------------
                  
                  Press 1 for generate Note
                  press 2 for view Note
                  press 3 for exit
             ''')
    user = int(input("Enter your choice:- "))

    if user == 1:
        # Generating a new E-Note
        username = input("Enter Python E-Note Generator Name: ")
        
        # Checking if the entered name is not a digit
        if username.isdigit():
            print("Error")
        else:
            usertitle = input("Enter Python E-Note Title: ")
            usercontent = input("Enter E-Note Content: ")
            
            # Opening a file in write mode and writing the E-Note details
            with open("new.txt", "w+") as a:
                a.write(f"Generator name:- {username}\n")
                a.write(f"E-Note Title:- {usertitle}\n")
                a.write(f"E-Note description:- {usercontent}\n")

    elif user == 2:
        # Viewing an existing E-Note
        display = input("Do you want to display your Note ['y'/'n']: ")

        if display.lower() == "y" or display.lower() == "yes":
            # Opening the file in read mode and printing its content
            with open("new.txt", "r") as re:
                print(re.read())

        # Setting status to False to exit the loop
        status = False

    elif user == 3:
        # Exiting the program
        print("You Exit!")
        status = False

     
         