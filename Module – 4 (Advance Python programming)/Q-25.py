# Q-24 Write a Python class named Circle constructed by a radius and two methods which will 
# compute the area and the perimeter of a circle

# Define a class named Circle
class Circle:
    # Initialize the Circle object with a radius 'r'
    def __init__(self, r):
        self.r = r  # Store the radius as an instance variable
    
    # Method to calculate the area of the circle
    def area(self):
        return 3.141 * self.r ** 2  # Return the area using the formula π * r^2
    
    # Method to calculate the perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * 3.141 * self.r  # Return the perimeter using the formula 2 * π * r

# Prompt the user to enter the radius of the circle
radius = int(input("Enter Radius : "))

# Create an instance of the Circle class with the given radius
circle = Circle(radius)

# Print the area and perimeter of the circle using the methods of the Circle class
print("Area of the circle :", circle.area())
print("Perimeter of the circle :", circle.perimeter())
