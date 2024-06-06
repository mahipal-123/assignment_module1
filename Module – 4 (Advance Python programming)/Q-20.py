# Q-20 Write python program that user to enter only odd numbers, else will raise an exception.

li = []  # Initialize an empty list to store numbers

try:
    for i in range(5):
        num = int(input("Enter Num : "))  # Prompt the user to enter a number
        if num % 2 == 0:
            raise Exception("Number must be odd")  # Raise an exception if the number is even
        li.append(num)  # Append the odd number to the list
except Exception as e:
    print(e)  # Print the error message if an exception is raised
