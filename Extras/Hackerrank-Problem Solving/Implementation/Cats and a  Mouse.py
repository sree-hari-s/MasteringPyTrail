import os


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distance_A = abs(x - z)
    distance_B = abs(y - z)
    if distance_A == distance_B:
        return "Mouse C"
    elif distance_A > distance_B:
        return "Cat B"
    else:
        return "Cat A"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + "\n")

    fptr.close()
