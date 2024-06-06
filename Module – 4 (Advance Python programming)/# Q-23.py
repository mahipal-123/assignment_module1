# Q-23 Write a Python class named Rectangle constructed by a length and width and a method which will 
# compute the area of a rectangle

# Define a class named Rectangle
class Rectangle:
    def area(self):
        l = int(input("Enter Length : "))  #  user to enter length
        b = int(input("Enter Breadth : "))  #  user to enter breadth
        return l * b  # Calculate and return the area of the rectangle

# Create an instance of the Rectangle class
rectangle = Rectangle()

# Print the area of the rectangle using the area() method
print("Area of Rectangle :", rectangle.area())
