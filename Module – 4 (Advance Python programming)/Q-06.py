# Q-06 Write a Python program to read a file line by line and store it into a list

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read all lines from the file into a list
li = file.readlines()

# Print the list of lines
print(li)

# Close the file
file.close()
