import random

randomCalculation = random.randint(1,3)

def selectionConverter(number):
    if number == 4:
        number = randomCalculation
    if number == 1:
        return "rock"
    elif number == 2:
         return "paper"
    elif number == 3:
        return "scissors"

print(selectionConverter(4))