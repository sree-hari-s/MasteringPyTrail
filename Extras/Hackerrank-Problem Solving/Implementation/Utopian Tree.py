import os


def utopianTree(n):
    growth = 1
    for i in range(n):
        if i % 2 == 0:
            growth *= 2
        else:
            growth += 1
    return growth


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + "\n")

    fptr.close()
