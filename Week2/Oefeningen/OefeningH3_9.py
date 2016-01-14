from enum import IntEnum, unique

__author__ = 'Owain'


@unique
class PocketEnum(IntEnum):
    def __str__(self):
        return self.name
    groen = 0
    rood = 1
    zwart = 2


def is_numeric(value):
    return value.isdigit()


def is_positive(value):
    return float(value) >= 0


def check_pocket(pocket):
    pocket = int(pocket)
    if pocket == 0:
        return str(PocketEnum(0))
    else:
        if pocket not in range(0, 11) and pocket not in range(18, 29):
            pocket += 1

        if pocket % 2 == 1:
            return str(PocketEnum(1))
        else:
            return str(PocketEnum(2))


def main():
    while True:
        digit = input("Vul een getal in (0-36)\n")

        if is_numeric(digit) and is_positive(digit):
            print("Deze pocket is {}".format(check_pocket(digit)))
        else:
            print("Dat is geen geldige invoer, probeer opnieuw!")
            continue


if __name__ == "__main__":
    main()
