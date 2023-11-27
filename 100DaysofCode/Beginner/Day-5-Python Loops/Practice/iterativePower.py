def iterativePower(a,n):
    """
    Time Complexity O(log(n))
    """
    result = 1
    while n > 0:
        if n % 2 != 0:
            result*=a
        a=a*a
        n=n//2
    return result

print(iterativePower(4,5))
