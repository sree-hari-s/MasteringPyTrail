l1 = [10,20,30]

l2 = l1[:]

t1 = (10,20,30)

t2 = t1[:]          # tuple having same element, has same id

s1 = "geeks"
s2 = s1[:]          # string of same value have same id

print(l1 is l2)

print(t1 is t2)

print(s1 is s2)