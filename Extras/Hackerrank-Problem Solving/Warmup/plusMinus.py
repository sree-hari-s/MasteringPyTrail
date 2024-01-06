def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zeros += 1
    print(f"{positive/len(arr)}\n{negative/len(arr)}\n{zeros/len(arr)}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
