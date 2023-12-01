def check_if_sorted(l):
    while True:
        i=0
        if l[i]>l[i+1]:
            return False
        i+=1
        return True

lst= [10,1,2,3,4,5,6,7,8,9,10]
print("Sorted list") if check_if_sorted(lst) else print("Not sorted list")