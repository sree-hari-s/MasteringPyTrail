import re

if __name__ == "__main__":
    N = int(input().strip())

    names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if re.search(".+@gmail.com", emailID):
            names.append(firstName)

    names.sort()

    for name in names:
        print(name)
