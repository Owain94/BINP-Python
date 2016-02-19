from random import randint
from Modules import CheckInput

__author__ = 'Owain'


def gooi(value):
    return randint(1, value)

digit = 0

while True:
    digit = input("Voer het aantal zijdes van de dobbelsteen in:\n")

    if CheckInput.is_numeric(digit):
        if CheckInput.is_positive(digit):
            break
        else:
            print("Dat is geen positief getal, probeer opnieuw!")
            continue
    else:
        print("Dat is geen geldig getal, probeer opnieuw!")
        continue

print("{} {}".format("Uw zogenaamde random int is:", gooi(int(digit))))
