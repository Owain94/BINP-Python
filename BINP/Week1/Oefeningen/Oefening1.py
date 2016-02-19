from Modules import CheckInput

__author__ = 'Owain'

char = None
digit = 0

while True:
    char = input("Voer een letter in:\n")
    if CheckInput.only_letters(char):
        if CheckInput.single_character(char):
            break
        else:
            print("Dat zijn meerdere letters, probeer opnieuw!")
    else:
        print("Dat is geen letter, probeer opnieuw!")
        continue

while True:
    digit = input("Voer een getal in:\n")

    if CheckInput.is_numeric(digit):
        if CheckInput.is_positive(digit):
            break
        else:
            print("Dat is geen positief getal, probeer opnieuw!")
            continue
    else:
        print("Dat is geen getal, probeer opnieuw!")
        continue

for x in range(0, int(digit)):
    print(char)

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
