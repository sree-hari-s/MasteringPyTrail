def LCM(a,b):
    result = max(a,b)
    
    while True:
        if result % a == 0 and result % b == 0:
            return result
        result+=1

a = int(input("A = "))
b = int(input("B = "))
print(f"LCM = {LCM(a,b)}")