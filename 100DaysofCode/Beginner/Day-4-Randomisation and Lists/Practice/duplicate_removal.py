"""
Remove Duplicates from a Sorted Array
"""


def remove_duplicates(arr, n):
    temp = [0] * n
    temp[0] = arr[0]
    result = 1
    for i in range(1, n):
        if temp[result - 1] != arr[i]:
            temp[result] = arr[i]
            result += 1
    for i in range(0, result):
        arr[i] = temp[i]
    return result


def remove_duplicates2(arr, n):
    result = 1
    for i in range(1, n):
        if arr[result - 1] != arr[i]:
            arr[result] = arr[i]
            result += 1
    return result


lst = [10, 20, 20, 30, 30, 30, 30]
print(remove_duplicates(lst, len(lst)))
