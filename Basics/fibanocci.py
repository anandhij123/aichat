num = int(input("Enter a number to generate Fibonacci series up to that number: "))
def fibonacci_series(n):
    fibonacci_series = []
    a, b = 0, 1
    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series
print("Fibonacci series up to", num, "is:", fibonacci_series(num))
