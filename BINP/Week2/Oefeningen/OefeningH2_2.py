from Modules import CheckInput
from math import pi

__author__ = 'Owain'

digit = 0


def bigger_than_5(value):
    return int(value) > 5


def smaller_than_pi(value):
    return int(value) < pi


def is_42(value):
    return int(value) == 42


def is_1(value):
    return int(value) == 1


while True:
    digit = input("Voer een getal in:\n")

    if CheckInput.is_numeric(digit):
        if CheckInput.is_positive(digit):
            break
        else:
            print("Dat is geen positief getal, probeer opnieuw!")
            continue
    else:
        print("Dat is geen geldig getal, probeer opnieuw!")
        continue

print("{} {}".format("Is dit getal groter dan 5?", bigger_than_5(digit)))
print("{} {}".format("Is dit getal kleiner dan pi?", smaller_than_pi(digit)))
print("{} {}".format("Is dit getal gelijk aan 42?", is_42(digit)))
print("{} {}".format("Is dit getal gelijk aan 1?", is_1(digit)))
