def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the 1st number?:\n"))
    for x in operations:
        print(x)
    operation_symbol = input("Pick an operation:\n")
    num2 = float(input("What's the 2nd number?:\n"))

    calc_function = operations[operation_symbol]
    first_answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    calc_on = True
    while calc_on:
        operation_symbol = input("Pick another operation:\n")
        num3 = float(input("What's the next number?:\n"))
        calc_function = operations[operation_symbol]
        next_answer = calc_function(first_answer, num3)

        print(f"{first_answer} {operation_symbol} {num3} = {next_answer}")



        more_calc = input(f"Type 'y' to continue calculating with {next_answer}, or type 'n' to start a new calculation:\n")
        if more_calc == "y":
            first_answer = next_answer
        elif more_calc == "n":
            calculator()

calculator()