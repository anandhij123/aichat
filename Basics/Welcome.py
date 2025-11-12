print("Welcome to Python programming")
'''print('o----')
print('||||')
name="Anandhi"

userName = input("What is your name")
favorite_color = input("what is your favorite color")
print (name + ' likes ' + favorite_color)

birth_year = input("Birth Year: ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(age)

weight_lbs = input('Weight(lbs)')
weight_kgs = int(weight_lbs) * 0.45
#String
course = 'Python for "Beginners"'
print(course[0]) #P
print(course[-2]) #s
print(course[0:3]) #Pyt
print(course[1:-1]) #ython for "Beginners
print(course[:]) #Python for "Beginners"

#Formatted String
first_name = "John"
last_name = "Smith"
message = f'{first_name}[{last_name}] is a coder' #John[Smith] is a coder
print (message)

#String methods
print(message.upper())
print(message.lower())
print(message.title())
print(message.find('h'))
print(message.replace('hn','se'))
print(message)
print('Python'in course)# use of in operator returns True if the keyword exist otherwise return false

#operator
x= 10**2
y=10+2*3/2+2**2+(1+2)# first precedence paranthesis followed by exponential and then multiplication/division followed by addition/subtraction
y+=10#Augmented assignment operator y=y+10
print(y)
#if loop
is_hot=False
is_cold=True
if is_hot:
    print("It is hot day")
elif is_cold:
    print("It is cold  day")
else:
    print("It is a beautiful day")
    print("Normal day")
#logical operators
has_good_credit=True
has_good_income=True
has_criminal_record=True
if (has_good_credit or has_good_income) and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")
#Project Weight
weight = int(input ('Weight:'))
unit = input ('(L)bs or (K)g:')
if unit.upper()== "L":
   print(weight * 0.45)
else:
    print(weight/0.45)# returns float, if weight//0.45, then returns int
#while loop
i=2
while i<=10:
    print (' * '*i)
    i=i+2
print("Done")
#project game
secret_number = 9
guess_count = 0
guess_limit = 2

while guess_count < guess_limit:
    guess_input = input("Enter the number: ")
    
    if guess_input.strip() == "":
        print("You didn't enter anything. Please enter a number.")
        continue
    
    try:
        guess = int(guess_input)
    except ValueError:
        print("That's not a valid number. Please enter a valid number.")
        continue
    
    if guess == secret_number:
        print('You won!')
        break
    else:
        print('You failed!')
    
    guess_count += 1

print("Game Over")


started = False
while True:  
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print('Car Started')
    elif command == "stop":   
        if started:
            started = False
            print("Car stopped")
        else:
            print('Car already stopped') 
    elif command == "help":   
        print("""
          Start - to start the car
          Stop -  to stop the car
          Quit -  to quit""" )
    elif command == "quit":
        print("Quitted")  
        break
    else:
        print('Sorry I dont understand')
#List
#Dictionary

phone=input("Enter the phone number: ")
number_names={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
        output +=number_names.get(ch,"!")

print(output)'''
#Function
def greet_user(first_name,last_name):
        print(f'Hi {first_name}{last_name}!')
        print('Welcome Aboard')


print('Start')
greet_user("Eva","smith")
print('Finish')
#Function parameters
def square(number):
        return(number*number)

print(square(3))


    



    


    


