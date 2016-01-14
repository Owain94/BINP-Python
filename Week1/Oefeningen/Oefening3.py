from Modules import CheckInput

__author__ = 'Owain'


def diminutive(val):
    return val + "tje"

value = None

while True:
    value = input("Voer een woord in:\n")

    if not CheckInput.single_character(value) and CheckInput.only_letters(value):
        break
    else:
        print("Dat is geen woord, probeer opnieuw!")
        continue

print(diminutive(value))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
