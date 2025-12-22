#Find largest number in a list
num_list=[23,45,12,67,34,89,10] 
largenum=num_list[0]
for n in num_list:
    if n>largenum:
        largenum=n  
print("The largest number in the list is:", largenum)
