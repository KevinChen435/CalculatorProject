def main():
    print("Here is the menu of Calculators")
    calc  = input("Please choose one of the options below: \n 1. Basic Calculator \n 2. Tip Calculator \n")
    if calc == "1":
        basiccalc()
    if calc == "2":
        tipcalc()

def basiccalc():
    operators = ["+","-","*","/","exit"]
    print('Welcome to the Basic Calculator')
    operator = ""
    while operator not in operators:
        operator = input("What operation?\n")
        if operator == "exit":
            exit()
    number1 = float(input("First Number?\n"))
    number2 = float(input("Second Number?\n"))
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
#basiccalc()
def tipcalc():
    print('Welcome to the Tip Calculator')
    operator = ""
    number1 = float(input("What is the price?\n"))
    number2 = float(input("What is the tax percentage?\n"))
    print("The tax is: " + str(round(100*(number1 * number2 * .01))/100))
    print("The final bill is " + str(round(100*(number1 * number2 * .01 + number1))/100))
main()