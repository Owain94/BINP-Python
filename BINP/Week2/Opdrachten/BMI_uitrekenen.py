from enum import IntEnum, unique
from Modules import CheckInput

__author__ = 'Owain'


@unique
class BmiEnum(IntEnum):
    def __str__(self) -> str:
        if self.name == "low":
            return "ondergewicht"
        elif self.name == "good":
            return "een gezond gewicht"
        elif self.name == "high":
            return "overgewicht"
    low = 0
    good = 1
    high = 2


def calculate_bmi(weight: str, height: str) -> float:
    return float(weight) / (float(height) ** 2)


def health(val: str) -> int:
    val = float(val)
    if val <= 18.5:
        return 0
    elif 18.5 < val <= 25:
        return 1
    else:
        return 2


def main() -> None:
    weight = 0
    height = 0

    while True:
        weight = input("Wat is uw gewicht (in kilogram)?\n")
        weight = weight.replace(",", ".")

        if (CheckInput.is_numeric(weight) or CheckInput.is_float(weight)) and CheckInput.is_positive(weight):
            break
        else:
            print("Dat is geen geldige invoer, probeer opnieuw!")
            continue

    while True:
        height = input("Wat is uw lengte (in centimeter)?\n")
        height = height.replace(",", ".")

        if CheckInput.is_numeric(height) and CheckInput.is_positive(height) and 2 <= len(height) <= 3:
            height = float(height) / 100
            break
        else:
            print("Dat is geen geldige invoer, probeer opnieuw!")
            continue

    bmi = calculate_bmi(weight, height)
    print("Uw BMI is: {0} u hebt {1}".format(str("{0:.2f}".format(bmi)).replace('.', ','), str(BmiEnum(health(bmi)))))

if __name__ == "__main__":
    main()
