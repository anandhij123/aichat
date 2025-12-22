name="Hello World"
number=float(123.4)
print(number)
a=[]
li=int(input("Enter the number of elements:"))#int(input()) converts the number of elements to an integer.
for i in range(li):
    element=input(f"Enter the number {i+1} :")
    a.append(element)
print(a)
#Another way of representing the above code
n = int(input("Enter the number of elements: "))
a = [input(f"Enter element {j+1}: ") for j in range(n)]
print("List:", a)

#Comprehensive list input through map
numbers=list(map(int,input("Enter the list of number separated by space").split()))
print("List:",numbers)