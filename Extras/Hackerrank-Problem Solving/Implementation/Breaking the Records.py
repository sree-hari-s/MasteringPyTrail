import os


def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    max_count = 0
    min_count = 0

    for i in range(len(scores)):
        if scores[i] > maximum:
            maximum = scores[i]
            max_count += 1
        elif scores[i] < minimum:
            minimum = scores[i]
            min_count += 1
    return [max_count, min_count]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
