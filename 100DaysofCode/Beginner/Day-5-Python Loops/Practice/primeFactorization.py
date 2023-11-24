from prime import *


def printPFactors(n):
    for i in range(2, n + 1):
        if prime3(i):
            x = i
            while n % x == 0:
                print(i)
                x *= i


n = int(input("Enter the number: "))
printPFactors(n)
