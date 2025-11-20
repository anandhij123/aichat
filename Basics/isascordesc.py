lst=input("Enter a list of numbers separated by spaces: ").split()
def is_asc_desc(lst):
    asc=True
    desc=True
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            desc=False
        if lst[i]>lst[i+1]:
            asc=False
    if asc:
        return "The list is in ascending order."
    elif desc:
        return "The list is in descending order."
    else:
        return "The list is neither in ascending nor in descending order."  
    
print(is_asc_desc([int(x) for x in lst]))   
    