def calc():
    operators = ["+","-","*","/","exit"]
    print('Welcome to the Calculator')
    operator = ""
    while operator not in operators:
        operator = input("What operation?\n")
        if operator == "exit":
            exit()
    number1 = int(input("First Number?\n"))
    number2 = int(input("Second Number?\n"))
    if operator == "+":
        print(str(number1 + number2))
    elif operator == "-":
        print(str(number1 - number2))
    elif operator == "*":
        print(str(number1 * number2))
    elif operator == "/":
        print(str(number1 / number2))
    else:
        exit()
calc()