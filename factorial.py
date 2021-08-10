# function
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * (factorial(n - 1)))

# input formatting and printing
x = int(input("Enter number here: "))
print(f"The factorial of {x} is {factorial(x)}")