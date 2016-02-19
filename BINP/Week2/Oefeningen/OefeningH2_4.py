from random import randint
from Modules import CheckInput

__author__ = 'Owain'


while True:
    a = randint(1, 100)
    b = randint(1, 100)

    digit = 0

    while True:
        digit = input("Wat is {} + {}?\n".format(a, b))

        if CheckInput.is_numeric(digit):
            if CheckInput.is_positive(digit):
                break
            else:
                print("Dat is geen positief getal, probeer opnieuw!")
                continue
        else:
            print("Dat is geen geldig getal, probeer opnieuw!")
            continue

    if digit == a + b:
        print("Dit klopt! {} + {} = {}".format(a, b, a + b))
    else:
        print("Dit klopt niet! {} + {} = {}".format(a, b, a + b))
