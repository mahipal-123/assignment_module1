# Q-10 Write a Python program to count the frequency of words in a file.

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read the entire content of the file
read = file.read()

# Split the content into words
words = read.split()

# Initialize an empty dictionary to hold word counts
di = {}

# Iterate over each word and count its occurrences
for word in words:
   di[word] = words.count(word)

# Print the dictionary containing word counts
print(di)

# Close the file
file.close()
