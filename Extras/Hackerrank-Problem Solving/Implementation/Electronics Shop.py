import os


def getMoneySpent(keyboards, drives, b):
    max_cost = -1

    for keyboard in keyboards:
        for drive in drives:
            total_cost = keyboard + drive
            if total_cost <= b and total_cost > max_cost:
                max_cost = total_cost

    return max_cost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + "\n")

    fptr.close()
