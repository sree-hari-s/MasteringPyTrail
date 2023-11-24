def prime(n):
    """
    Time Complexity is O(n)
    """
    if n <= 1:
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return True if count == 2 else False


def prime2(n):
    """
    Time Complexity is O(root(n))
    """
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime3(n):
    """
    Most efficient method to find prime number
    """
    if n == 1:
        return False
    if n == 2 or n==3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    n = int(input("Enter a number to check if prime: "))
    print("Prime") if prime3(n) else print("Not prime")
