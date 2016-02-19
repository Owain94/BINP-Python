from math import pi
from Modules import CheckInput

__author__ = 'Owain'


def surface(val):
    return pi * (float(val) ** 2)

digit = 0

while True:
    digit = input("Voer een radius in:\n")

    if CheckInput.is_float(digit):
        if CheckInput.is_positive(digit):
            break
        else:
            print("Dat is geen positief getal, probeer opnieuw!")
            continue
    else:
        print("Dat is geen geldig getal, probeer opnieuw!")
        continue

print("{} {}".format("Het oppervlakte van de cirkel is:", str("{0:.2f}".format(surface(digit))).replace('.', ',')))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
