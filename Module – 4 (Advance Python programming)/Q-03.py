# Q-03 Write a Python program to append text to a file and display the text.
# Open 'writefile.txt' in append and read mode ('a+')
file = open('writefile.txt', 'a+')

# Write two lines of text to the file
file.write("What are you doing?\n")
file.write("Have a nice day.")

# Move the file pointer to the beginning
file.seek(0)

# Read and print the file's content
print(file.read())

# Close the file
file.close()