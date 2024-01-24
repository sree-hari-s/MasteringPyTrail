import os


def bonAppetit(bill, k, b):
    total = 0
    for i in range(len(bill)):
        if i != k:
            total += bill[i]
    to_pay = total // 2
    if to_pay == b:
        print("Bon Appetit")
    else:
        print(b - to_pay)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
