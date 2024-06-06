# Q-11 Write a Python program to write a list to a file.

# List to be written to the file
li = [1, 2, 3, 4, 5, 6, 7]

# Open the file 'writefile.txt' in write mode ('w')
file = open('writefile.txt', 'w')

# Convert the list to a string representation
string = str(li)

# Write the string representation of the list to the file
file.write(string)

# Close the file
file.close()
