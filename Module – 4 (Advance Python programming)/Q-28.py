#Q-28 What is used to check whether an object o is an instance of class A?
''' To check object o is an instance of class A :

We can use isinstance method with object as first and class as second parameter.'''

class A:
   pass

o=A()

check = isinstance(o,A) # output: True