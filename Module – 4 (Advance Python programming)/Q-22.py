#Q-22 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
''' To define a class in python class keyword is used.
class Student():
   pass
Self is a default parameter provided by the python, which needs to be specified while defining a method.

It works similar to the pointer in C++.

Example :
# define a class
class Student():
   # define a method
   def greetings(self): # default self parameter
      print("Welcome, Have a good day.")

# creating a object
student=Student()

# using the class method
student.greetings() '''