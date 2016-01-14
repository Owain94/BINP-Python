from re import match

__author__ = 'Owain'


def is_numeric(value):
    return value.isdigit()


def is_positive(value):
    return float(value) > 0


def is_float(val):
    return not match("^\d+?\.\d+?$", val) is None


def calculate_area(length, width):
    return float(length) * float(width)


def main():
    length = None
    rectangle = None

    for i in range(1, 5):
        while True:
            if i % 2 == 1:
                string = "Voer de lengte in:\n"
            else:
                string = "Voor de breedte in:\n"

            value = input(string)

            if (is_numeric(value) or is_float(value)) and is_positive(value):
                if i % 2 == 1:
                    length = value
                else:
                    if i == 2:
                        rectangle = calculate_area(length, value)
                    else:
                        area = calculate_area(length, value)

                        if rectangle > area:
                            print("rechthoek 1 is groter dan rechthoek 2")
                        else:
                            print("rechthoek 2 is groter dan rechthoek 1")
                break
            else:
                print("Dat is geen geldige invoer, probeer opnieuw!")
                continue

if __name__ == "__main__":
    main()
