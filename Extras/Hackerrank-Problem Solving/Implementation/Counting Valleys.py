import os


def countingValleys(steps, path):
    level, valley = 0, 0
    for i in range(steps):
        if path[i] == "U":
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1
    return valley


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + "\n")

    fptr.close()
