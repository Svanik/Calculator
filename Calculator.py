
"""Calculator App Made by: Svanik Dani."""
print('''
''')
print("Starting Calculator")
print("(Made by Svanik Dani)")
print("Enjoy Using The Calculator")


def enternum():
    """Entering  num."""
    num = input("Enter a number: ")
    print(f"Number is {num}")
    confirmation = input("Please confirm by typing (y/n)")
    if confirmation == "y" or confirmation == "Y":
        print("Confirmed")
    elif confirmation == "n" or confirmation == "N":
        print("Reseting Calculator")
        enternum()
    else:
        print("Invalid input")
        enternum()
    return num


def opperations():
    """Entering opperation."""
    opperation = input("Enter the Math Opperation (+,-,*,/): ")
    print(f'Opperation is {opperation}')
    confirmation = input("Please confirm by typing (y/n)")
    if confirmation == "y" or confirmation == "Y":
        print("Confirmed")
    elif confirmation == "n" or confirmation == "N":
        print("Reseting Calculator")
        opperations()
    else:
        print("Invalid input")
        opperations()
    return opperation


def caclculation():
    """For caclculation."""
    if op == "+":
        x = num1 + num2
        x = round(x, 5)
        print(f"{num1} + {num2} = {x}")
    elif op == "-":
        q = num1 - num2
        q = round(q, 5)
        print(f"{num1} - {num2} = {q}")
    elif op == "*":
        y = num1 * num2
        y = round(y, 5)
        print(f"{num1} * {num2} = {y}")
    elif op == "/":
        z = num1 / num2
        z = round(z, 5)
        print(f"{num1} / {num2} = {z}")


x = 1
while x == 1:
    num1 = enternum()
    num1 = float(num1)
    op = opperations()
    num2 = enternum()
    num2 = float(num2)
    caclculation()
    confirm = input("Would you like to perform another caclculation.(y/n)")
    if confirm == "y" or confirm == "Y":
        x = 1
    elif confirm == "n" or confirm == "N":
        print("Exiting Calculator")
        x = -1
    else:
        print("Invalid input")
