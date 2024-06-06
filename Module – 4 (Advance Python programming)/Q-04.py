# Q-04 Write a Python program to read first n lines of a file.

# The user to enter the number of lines to display and convert the input to an integer
n = int(input("Enter the num of lines you want to show? : "))

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Loop to read and print the specified number of lines
for i in range(n):
   print(file.readline(), end="")

# Close the file
file.close()
