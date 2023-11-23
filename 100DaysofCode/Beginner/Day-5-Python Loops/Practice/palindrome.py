n = int(input("Enter a number to check if palindrome: "))
temp = n
rev = 0
while temp != 0:
    r = temp%10 
    rev = rev*10+r
    temp //=10
print(rev)
if n == rev:
    print("Palindrome")
else:
    print("Not palindrome")