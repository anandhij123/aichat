"""Program to find Loves me or Loves Me Not between two people based on their number of petals.  """
num_petals1=int(input("Enter the number of petals for person 1: "))
for i in range(num_petals1):
    if i%2==0: 
      last_word="Loves me"  
    else:
      last_word="Loves Me Not" 
print("The final result is:", last_word)

