"""
# List Comprehension Hackerrank
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""
if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ls = [[i, n, w] for i in range(x + 1) for n in range(y + 1) for w in range(z + 1)]
new_ls = [i if i[0] + i[1] + i[2] != n else "" for i in ls]
new_ls = [i for i in new_ls if i != ""]
print(new_ls)
