# Q-12 Write a Python program to copy the contents of a file to another file.

# Open 'readfile.txt' in read mode and read its content
with open('readfile.txt', 'r') as file:
    readfile = file.read()

# Open 'writefile.txt' in write mode and write the content of readfile into it
with open('writefile.txt', 'w') as file:
    file.write(readfile)
