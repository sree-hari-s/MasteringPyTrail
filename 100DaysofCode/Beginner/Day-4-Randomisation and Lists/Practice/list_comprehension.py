#
def even_nos():
    l1 = [x for x in range(11) if x%2 == 0]
    return l1

def get_smaller_elements(l,x):
    l2 = [a for a in l if a<x]
    return l2

def odd_even(l):
    even = [x for x in l if x%2 == 0]
    odd = [x for x in l if x%2 != 0]
    return even,odd

l1 = even_nos()
print(l1)
print(get_smaller_elements(l1,3))

lst = [1,2,3,4,5,6,7,8,9,10,11]
print(odd_even(lst))