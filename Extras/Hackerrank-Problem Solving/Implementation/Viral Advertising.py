import os


def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(1, n + 1):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + "\n")

    fptr.close()
