def calculate_bmi(height, weight):
  """Calculates the Body Mass Index (BMI) of a person.

  Args:
    height: The height in meters.
    weight: The weight in kilograms.

  Returns:
    The BMI as a float.
  """

  bmi = weight / (height ** 2)
  return bmi


def main():
  """Prompts the user to enter their height and weight, calculates their BMI, and prints the result."""

  height = float(input("Enter your height in meters: "))
  weight = float(input("Enter your weight in kilograms: "))

  bmi = calculate_bmi(height, weight)

  print(f"Your BMI is {bmi}.")

  if bmi < 18.5:
    print("You are underweight.")
  elif bmi >= 18.5 and bmi < 25.0:
    print("You are a normal weight.")
  elif bmi >= 25.0 and bmi < 30.0:
    print("You are overweight.")
  else:
    print("You are obese.")


if __name__ == "__main__":
  main()