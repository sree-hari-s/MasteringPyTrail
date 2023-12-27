"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""
import os


def diagonalDifference(arr):
    primary_dia_sum = 0
    secondary_dia_sum = 0
    length = len(arr[0])
    for i in range(length):
        primary_dia_sum += arr[i][i]
        secondary_dia_sum += arr[i][length - i - 1]
    return abs(primary_dia_sum - secondary_dia_sum)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
