#Method 1:Define value directly in the list
mylist=[1,2,3,4,5]
print(type(mylist))
# Method 2:Define value in the list of particular pattern
# syntax:[expression iterator condition]
sqr_list=[i**2 for i in range(1,20) if i%2==1] 
print(sqr_list)
# Method 3:Define value in the list using function and filter
# syntax:list(filter(function,iterator))
list1=list(range (2,50))
print(list1)
# Method 4:Define value in the list using function and filter
# syntax:list(filter(function,iterator))
odd_list=list(filter(lambda x:x%2==1,range(1,50))) #lambda arguments: expression
print(odd_list)
unsort_list=[45,12,3,78,23,5 ]
print(sorted(unsort_list))
print(mylist[0])
mylist.extend([6,7,8])#adds multiple elements to the end of the list
print(mylist)
mylist.append(9) #adds single element to the end of the list
mylist.reverse()
print(mylist)

