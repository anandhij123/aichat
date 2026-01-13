a=10
b=2
c=a
# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

#Comparison
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical
print("*******Logical Operations*******")
print(True and False)
print(True or False)
print(not True)

print("*******Identity Operations*******")
print(a is b)
print(a is c)
print("*******Membership Operations*******")
li=[10,20,30,40,50]
li2=24
li3=20
print(li2 in li)
print(li3 in li)
print(li2 not in li)    
print("*******Bitwise Operations*******")
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print("*******Ternary Operations*******")
min = a if a < b else b
print(min)