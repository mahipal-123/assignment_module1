# Q-09 Write a Python program to count the number of lines in a text file.

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read all lines from the file into a list
read = file.readlines()

# Print the number of lines in the file
print("Number of lines in file:", len(read))

# Close the file
file.close()
