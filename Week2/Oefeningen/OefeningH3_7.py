__author__ = 'Owain'


class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


def colors(color):
    color = str(color)
    for case in Switch(color):
        if case('rood'):
            return 1
        if case('blauw'):
            return 2
        if case('geel'):
            return 3
        if case('3'):
            return "paars"
        if case('4'):
            return "oranje"
        if case('5'):
            return "groen"


def main():
    primary = ['rood', 'blauw', 'geel']

    color1 = None
    color2 = None

    while True:
        color1 = input("Vul een primaire kleur in (rood blauw of geel)\n")
        color1 = color1.lower()

        if color1 in primary:
            break
        else:
            print("Dat is geen geldige input! probeer opnieuw!")

    while True:
        color2 = input("Vul nog een primaire kleur in (rood blauw of geel)\n")
        color2 = color2.lower()

        if color2 in primary:
            break
        else:
            print("Dat is geen geldige input! probeer opnieuw!")

    if color1 == color2:
        print("Als je {} met {} mengt krijg je {}".format(color1, color2, color1))
    else:
        print("Als je {} met {} mengt krijg je {}".format(color1, color2, colors(int(colors(color1) + colors(color2)))))


if __name__ == "__main__":
    main()
