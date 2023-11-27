def power(a,n):
    """
    Time complexity is O(n)
    """
    result = 1
    for i in range(n):
        result*=a
    print(result)

def power2(a,n):
    """
    Time complexity is theta(log(n))
    """
    if n == 0:
        return 1
    temp = power2(a,n//2)
    temp = temp*temp
    if n%2 == 0:
        return temp
    else:
        return temp*a

print(power2(2,3))