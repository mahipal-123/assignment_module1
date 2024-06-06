# Q-19 How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

'''
   - To handle an Exception with Try/Excepty/Finally block.
   - Give Try block the code that might raise an exception.
   - If there is an exception the except block is triggered.
   - And the finally block is executed everytime
'''

try:
    num = input("Enter a num : ")  # Prompt the user to enter a number
    num = int(num)  # Convert the input to an integer
    print("Your Number :", num)  # Print the number if conversion succeeds
except ValueError as e:
    print(f"Error : {e}")  # Handle the ValueError if input cannot be converted to an integer
finally:
    print("Thank You for using !!")  # Execute this block regardless of whether an exception occurred

   
'''
   Here, try block might raise an valueError so we provide an ValueError except block to handle the exception.
   And the finally block is executed regardless of exception being found or not.
'''