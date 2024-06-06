#Q-26 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
#Inheritance
#Inheritance in python refers to subclass or derived class to inherit properties of superclass or base class.
# Define a parent class named School
class School:
    def __init__(self, name, no):
        self.name = name  # Initialize 'name' attribute
        self.no = no  # Initialize 'no' attribute

# Define a child class named Student, inheriting from School
class Student(School):
    def marksheet(self, marks):
        self.marks = marks  # Initialize 'marks' attribute
        # Return a formatted string containing name, roll number, and marks
        return f"Name : {self.name} | Roll no : {self.no} | Marks : {self.marks}"

# Create an instance of the Student class
student = Student("Mahipal", 6)

# Print the result of the marksheet method with marks passed as argument
print(student.marksheet(91))


#Constructor :
''' In python init is a dunder method, they are called automatically on certain events related to class.

The init method gets called automatically when the object is created and it is also knows as Constructor.
'''
