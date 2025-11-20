x=input("Enter first number: ")
y=input("Enter second number: ")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
print("GCD of", x, "and", y, "is", gcd(int(x), int(y)))
