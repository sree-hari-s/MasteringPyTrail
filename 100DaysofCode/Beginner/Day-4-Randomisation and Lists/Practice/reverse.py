def reverse_list(l):
    return l[::-1]


def reverse_list2(l):
    i = 0
    j = len(l) - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l


print(reverse_list2([1, 2, 3, 4]))
