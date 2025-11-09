# Take Input from  user snd calculate the area of rectangle and circle save it to the dictionary
import math
length=float(input("Enter your Length: "))
width=float(input("Enter your Length: "))
radius=float(input("Enter your radius: "))
pi=math.pi
rectangle_area=length*width
circle_area=pi*(radius**2)
print("Area of Rectangle: ",round(rectangle_area,2))
print("Area of Rectangle: ",round(circle_area,2))
