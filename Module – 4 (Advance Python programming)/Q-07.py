# Q-07 Write a Python program to read a file line by line store it into a variable.

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read all lines from the file into a list
li = file.readlines()

# Print the list of lines
print(li)

# Close the file
file.close()
