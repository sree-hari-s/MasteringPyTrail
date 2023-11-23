def GCD(a, b):
    """
    Function to find Greatest Common divisor using Euclidean Algorithm
    """
    while a != b:
        if a > b:
            a = a - b
            print("a", a)
        else:
            b = b - a
            print("b", b)
    return a


def GCD_optimized(a, b):
    """
    Optimized Euclidean Algorithm using Recursive method
    """
    if b == 0:
        return a
    return GCD_optimized(b, a % b)


a = int(input("A = "))
b = int(input("B = "))
print(f"GCD = {GCD(a,b)}")
