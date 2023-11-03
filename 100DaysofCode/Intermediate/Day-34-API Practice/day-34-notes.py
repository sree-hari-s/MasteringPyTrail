age : int

age = 'twelve'

print(type(age))
"""
Type Hints
"""
def learners_license(age:int)->bool:
    if age>18:
        return True
    else:
        return False

if learners_license(20):
    print("You can drive")
else:
    print("Fine of Rs 10000")