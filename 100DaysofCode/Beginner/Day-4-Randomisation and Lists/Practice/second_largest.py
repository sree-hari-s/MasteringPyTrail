def sec_largest_element(l):
    largest = l[0]
    second_largest = 0
    for i in l:
        if i > largest:
            largest = i
    for i in l:
        if i>second_largest and i < largest:
            second_largest = i
    return second_largest
        

def get_second_largest(l):
    """
    Efficient solution , only one traversal required
    """
    if len(l)<=1:
        return None
    largest = l[0]
    sec_largest= None
    for x in l[1:]:
        if x>largest:
            sec_largest = largest
            largest=x
        elif x!=largest:
            if sec_largest==None or sec_largest<x:
                sec_largest=x
    return sec_largest

lst= [1,2,3,4,5,6,7,8,9,10]
print(sec_largest_element(lst))