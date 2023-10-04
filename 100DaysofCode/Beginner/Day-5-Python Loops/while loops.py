count= 0
while count<10:
    count += 1
    print(count)
    if count<=5:
        pass
    if count <=5:
        continue
    if count <=5:
        break
    
print("\n")

"""
python allows us to write an else in while loop
to understand what to do if while loop fails.
"""
count1 = 1
while count1< 5:
    print(count1)
    count1 += 1
else:
    print(count1)