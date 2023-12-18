if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    num_swaps = 0

    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                num_swaps += 1

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")