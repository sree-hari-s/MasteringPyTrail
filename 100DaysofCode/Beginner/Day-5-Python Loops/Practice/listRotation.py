# Direct Methods

l = [10,20,30,40]
l = l[1:]+l[0:1]
print(l)

l.append(l.pop(0))
print(l)

# Loop method

def rotate_left(arr):
    n = len(arr)
    x = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = x
    return arr

print(rotate_left(l))