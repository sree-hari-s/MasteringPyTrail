"""
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
"""

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
sum = int(first_digit)+int(second_digit)
print(f"{first_digit}+{second_digit} = {sum}")


def sum_digits(number):
    """
    This function sums the digits of a number.

    Args:
      number: The number to sum the digits of.

    Returns:
      The sum of the digits of the number.
    """
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum


def main():
    number = input("Type a number: ")
    print(f"The sum of the digits of {number} is {sum_digits(number)}")


if __name__ == "__main__":
    main()