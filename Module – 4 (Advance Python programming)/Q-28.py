#Q-28 What is used to check whether an object o is an instance of class A?
''' To check object o is an instance of class A :

We can use isinstance method with object as first and class as second parameter.'''

# Define a class named A
class A:
    pass

# Create an instance of class A
o = A()

# Check if 'o' is an instance of class A
check = isinstance(o, A)

# Print the result
print(check)  # Output: True
