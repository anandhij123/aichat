product=1
count=int(input("Enter the count of numbers : "))
for num in range(count):
    i=float(input(f"Enter the real number#{num+1} : "))
    product = product*i
    
print(product)