#Q-26 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
#Inheritance
#Inheritance in python refers to subclass or derived class to inherit properties of superclass or base class.
class School:
   def __init__(self,name,no):
      self.name=name
      self.no=no

class Student(School):
   def marksheet(self,marks):
      self.marks=marks
      return f"Name : {self.name} | Roll no : {self.no} | Marks : {self.marks}"

student=Student("Tirth",5)
print(student.marksheet(98))

#Constructor :
''' In python init is a dunder method, they are called automatically on certain events related to class.

The init method gets called automatically when the object is created and it is also knows as Constructor.
'''