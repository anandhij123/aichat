"""Give two positive integer representing the length and the width of a rectangle,determine how many rectangle can fit inside the rectangle."""
length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))  
def rectCount(l, w):
    area=l*w
    count=0
    for i in range(1, l+1):
        for j in range(1, w+1):
            count+= (l - i + 1) * (w - j + 1)
    return count
print("Number of rectangles that can fit inside the rectangle is:", rectCount(length, width))
