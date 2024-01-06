import os


def timeConversion(s):
    hours, minutes, seconds = map(int, s[:-2].split(":"))
    period = s[-2:]

    if period == "PM" and hours != 12:
        hours += 12
    elif period == "AM" and minutes == 12:
        hours = 0

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
