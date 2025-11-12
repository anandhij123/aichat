num_input= input("Enter the number: ")
    
if num_input.strip() == "":
    print("You didn't enter anything. Please enter a number.")
   
    
try:
    check_num = int(num_input)
except ValueError:
        print("That's not a valid number. Please enter a valid number.")
        
    
if check_num%2==0:
    print('Its a Even number!')
    
else:
    print('Its a Odd number!')