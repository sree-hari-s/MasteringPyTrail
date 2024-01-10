import os


def hurdleRace(k, height):
    highest = max(height)
    if highest > k:
        return highest-k
    return 0

if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
