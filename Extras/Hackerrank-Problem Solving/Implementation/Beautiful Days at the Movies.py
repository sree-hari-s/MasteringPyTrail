import os


def beautifulDays(i, j, k):
    count = 0
    for l in range(i, j + 1):
        n = str(l)[::-1]
        if abs(l - int(n)) % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + "\n")

    fptr.close()
