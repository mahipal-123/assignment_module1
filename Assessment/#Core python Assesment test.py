import datetime

def main_menu():
    """
    Displays the main menu of the Python E-Notebook.
    """
    menu = """
              Welcome To Python E-Notebook

              Press 1 for Generate Note
              Press 2 for View Note
              Press 3 For Exit
         """
    return menu

def generate_note():
    """
    Generates a new E-Note and writes it to a file.
    """
    name = input("Enter Python E-Note Generator Name: ")
    title = input("Enter Python E-Note Title: ")
    content = input("Enter E-Note Content: ")

    with open("Python_E-note.txt", 'a') as f:
        f.write("==================================\n")
        now = datetime.datetime.now()
        f.write(f"{now}\n")
        f.write(f"E-Note Title: {title}\n")
        f.write(f"E-Note Description: {content}\n")
        f.write(f"E-Note Generator: {name}\n")

def view_notes():
    """
    Displays all the E-Notes stored in the file.
    """
    try:
        with open("Python_E-note.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")

status = True

while status:
    print(main_menu())
    choice = input("Enter Your Choice: ")

    if choice == '1':
        generate_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        print("Thank You")
        status = False
    else:
        print("Please Enter a Valid Choice!!!")
