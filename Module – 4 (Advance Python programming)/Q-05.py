# Q-05 Write a Python program to read last n lines of a file.

# Number of lines to read from the end of the file
a = 3

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read all lines from the file and get the last 'a' lines
read = file.readlines()[-a:]

# Loop through the selected lines and print each one
for line in read:
   print(line, end="")

# Close the file
file.close()
