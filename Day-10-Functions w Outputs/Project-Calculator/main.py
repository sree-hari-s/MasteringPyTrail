from art import logo
print(logo)

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1 / number2

def multiply(number1, number2):
    return number1 * number2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("Enter the first number ? "))
    for each_symbol in operations:
        print(each_symbol)
    end_program = False
    while not end_program:
        operation_symbol =input("Pick an operation from the line above: ")
        num2 = float(input("Enter the next number ? "))
        
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type 'yes' to continue calculating with {answer}, type 'no' to start a new calculation or Type 'quit' to exit the program:")
        if choice == "yes":
            num1 = answer
        elif choice == "no":
            end_program = False
            calculator()
        else:
            print("Good Bye")
            end_program = True

calculator()