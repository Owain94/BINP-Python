# from typing import Iterator

__author__ = 'Owain'


class Switch(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.fall = False

    # def __iter__(self) -> Iterator:
    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args: int) -> bool:
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


def is_numeric(value: str) -> bool:
    return value.isdigit()


def is_positive(value: str) -> bool:
    return float(value) >= 0


def main() -> None:
    var = [0, 0, 0, 0]

    for i in range(1, 5):
        while True:
            inp = input("voer het {}e getal in:\n".format(i))

            if is_numeric(inp):
                value = int(inp)

                for case in Switch(i):
                    if case(1):
                        var[0] = value
                    if case(2):
                        var[1] = value
                    if case(3):
                        var[2] = value
                    if case(4):
                        var[3] = value

                break
            else:
                print("Dat is geen geldige invoer, probeer opnieuw!")
                continue

    if var[0] <= var[1] != var[0]:
        print(1)

    if var[2] > var[0] or var[1] == var[3]:
        print(2)

    if (var[3] < var[2] and var[1] > var[0]) or var[3] < var[0]:
        print("3a")
    elif (var[3] < var[2] and var[1] > var[0]) or var[3] < var[0]:
        print("3b")
    else:
        print("3c")

if __name__ == "__main__":
    main()
