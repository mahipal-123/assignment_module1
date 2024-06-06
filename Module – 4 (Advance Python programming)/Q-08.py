# Q-08 Write a python program to find the longest words.

# Open the file 'readfile.txt' in read mode ('r')
file = open('readfile.txt', 'r')

# Read the entire file content and split it into words
words = file.read().split()

# Initialize a variable to hold the longest word
longest_word = ""

# Iterate over each word to find the longest one
for word in words:
   if len(longest_word) < len(word):
      longest_word = word

# Print the longest word found
print("Longest word:", longest_word)

# Close the file
file.close()
