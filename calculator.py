import re

previous = 0
run = True

print("Welcome to calculator App!")
print("type quit to exit")

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("enter your value:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.\"]', " ", equation)
        if previous == 0:
            previous = eval(str(equation))
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()

