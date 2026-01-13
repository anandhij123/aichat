import math
"""h=input("Enter the height of the triangle: ")
l=input("Enter the breadth of the triangle:")
area=(1/2)*int(h)*int(l)
print(area)"""
#Area of 3 sided triangle
a=int(input("Enter the length of the side 1 of the triangle: "))
b=int(input("Enter the length of the side 1 of the triangle: "))
c=int(input("Enter the length of the side 1 of the triangle: "))
s=(a+b+c)/2
A=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(A)

#Area of circle pir2
r=int(input("Enter the radius of the circle: "))
area=math.pi*r*r
print(area)