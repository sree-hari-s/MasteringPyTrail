def divisors(n):
    """
    Prints all divisors of the given number
    Time Complexity is Linear 
    """
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

def divisors2(n):
    """
    Better time complexity but the output is not printed in a sorted order
    """
    i = 1
    while (i*i<=n):
        if n%i == 0:
            print(i)
            if i!=n/i:
                print(int(n/i))
        i+=1

def divisors3(n):
    """
    All the divisors are printed in a sorted order
    Time Complexity is theta of n only
    """
    i = 1
    while (i*i<=n):
        if n%i == 0:
            print(i)
        i+=1
    while (i>=1):
        if n%i == 0:
            print(int(n/i))
        i-=1

if __name__ == "__main__":
    n = int(input("Enter a number:"))
    divisors3(n)
