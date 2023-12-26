def prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    print("Prime") if prime(n) else print("Not prime")