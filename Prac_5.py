# Practical No 5

# program1
import math
side = int(input("Enter the Side of the square: "))
area = pow(side,2)
print("The Area of the Square is: ",area)
perimeter = 4*side
print("The Perimeter of the Square is: ",perimeter)

# program2
radius = int(input("\nEnter the Radius: "))
height  = int(input("Enter the Height: "))

volume = math.pi*pow(radius,2)*(height/3)
print("The Volume of the Cube is : ",volume)