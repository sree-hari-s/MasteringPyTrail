import os


def angryProfessor(k, a):
    count = 0
    for i in range(len(a)):
        if a[i] <= 0:
            count += 1
    return "NO" if count >= k else "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + "\n")

    fptr.close()
