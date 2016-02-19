from re import match

__author__ = 'Owain'


def is_numeric(value):
    return value.isdigit()


def is_positive(value):
    return float(value) > 0


def is_float(val):
    return not match("^\d+?\.\d+?$", val) is None


def convert_to_newton(val):
    return float(val) * 9.8


def main():
    while True:
        digit = input("Voor het aantal kilogram in:\n")
        digit = digit.replace(",", ".")

        if (is_float(digit) or is_numeric(digit)) and is_positive(digit):
            result = convert_to_newton(digit)

            if result < 100:
                print("Dit object weegt te weinig")
            elif result > 500:
                print("Dit object weegt te zwaar")
            else:
                print("Het gewicht van dit object is {0:.2f}N".format(convert_to_newton(digit)).replace('.', ','))
        else:
            print("Dat is geen geldige invoer, probeer opnieuw!")
            continue


if __name__ == "__main__":
    main()
