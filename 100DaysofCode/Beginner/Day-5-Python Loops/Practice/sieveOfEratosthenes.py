"""
Prints the list of prime numbers upto N
"""
"""
Naive approach to solve the problem

from prime import prime

n = int(input())
for i in range(n):
    if prime(i):
        print(i,end=" ")
"""

def sieve(n):
    """
    Time complexity O(n*root(n))
    """
    if n <=1:
        return 1

    isPrime = [True]*(n+1)
    print(isPrime)
    i = 2 
    
    while i*i<=n:
        if isPrime[i]:
            for j in range(2*i,n+1,i):
                isPrime[j] = False
        i+=1
    print(isPrime)
    for i in range(2,n+1):
        if isPrime[i]:
            print(i,end=" ")

def sieve2(n):
    """
    Time complexity O(nloglog(n))
    """
    if n <=1:
        return 1
    isPrime = [True]*(n+1)
    i=2
    while i <=n:
        if isPrime[i]:
            print(i,end=" ")
            for j in range(i*i,n+1,i):
                isPrime[j] = False
        i+=1

if __name__ == "__main__":
    n = int(input("Enter a number : "))
    sieve2(n)
