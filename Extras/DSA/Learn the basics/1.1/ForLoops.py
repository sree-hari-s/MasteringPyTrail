"""
Nth Fibonacci Number
https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
"""


def F(n):
    if n==1:
        return 1
    elif n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)


n=int(input())
a=F(n)
print (a)