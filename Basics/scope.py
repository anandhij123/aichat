msg="Welcome to Python" #global scope
def greet():
   msg="Inside function" #local scope
   print(msg)
print(msg)
greet()