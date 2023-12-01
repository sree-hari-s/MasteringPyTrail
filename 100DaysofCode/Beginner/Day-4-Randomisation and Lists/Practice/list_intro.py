l = [10,20,30,40,50,60]
print(l) # [10, 20, 30, 40, 50, 60]
l.insert(1,15) 
print(l) # [10, 15, 20, 30, 40, 50, 60]
print(15 in l)
print(l.count(30))
print(l.index(30))
print(l.index(30,2,7)) # element to search ,starting index in inclusive ending index is exclusive

l.remove(30)
print(l)
print(l.pop()) # removes last element from list
print(l)
del l[1] # remove item at index 1
print(l) 

l=[10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)
