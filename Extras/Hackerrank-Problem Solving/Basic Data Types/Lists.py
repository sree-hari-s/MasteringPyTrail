if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        s = list(input().split())
        if s[0] == "insert":
            arr.insert(int(s[1]), int(s[2]))
        if s[0] == "remove":
            arr.remove(int(s[1]))
        if s[0] == "append":
            arr.append(int(s[1]))
        if s[0] == "sort":
            arr.sort()
        if s[0] == "pop":
            arr.pop()
        if s[0] == "reverse":
            arr.reverse()
        if s[0] == "print":
            print(arr)
