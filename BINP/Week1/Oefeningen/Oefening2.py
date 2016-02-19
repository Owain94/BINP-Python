from Modules import CheckInput

__author__ = 'Owain'


def convert_to_miles(val):
    return float(val) * 0.6214

digit = 0

while True:
    digit = input("Voer een getal in:\n")

    if CheckInput.is_float(digit):
        if CheckInput.is_positive(digit):
            break
        else:
            print("Dat is geen positief getal, probeer opnieuw!")
            continue
    else:
        print("Dat is geen geldig getal, probeer opnieuw!")
        continue

print(convert_to_miles(digit))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
