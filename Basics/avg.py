n=int(input("Enter the count of integers : "))
sum=0
for i in range(n):
    num=int(input(f"Enter the number#{i+1} : "))
    sum=sum+num
avg=sum/n
print(f"The average is: {avg}")