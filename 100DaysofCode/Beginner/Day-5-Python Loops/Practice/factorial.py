n = int(input("Enter a number to check factorial : "))

def factorial(n):
    """
    Returns the factorial using Recursive method
    """
    if n == 0:
        return 1
    return n*factorial(n-1)

def factorial1(n):
    """
    Returns the factorial using iterative method
    """
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

print(f"Factorial of {n} is {factorial1(n)}")