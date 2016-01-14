__author__ = 'Owain'


def pyramid(size: int, diamond: bool) -> list:
    val = size
    li = []

    for i in range(size):
        row = str(val) * (2 * i + 1)
        li.append(row.center(2 * size))
        val -= 1

    if diamond:
        i = 0
        for j in range(size * 2, 0, -2):
            if i != 0:
                row = str((j - 1) * str(i + 1))
                li.append(row.center(2 * size))
            i += 1

    return li


def main() -> None:
    while True:
        inp = input("voer een getal in:\n")

        # Ik maak het mezelf hier niet lastig en ik ben niet aan het 'uitsloven'
        # Deze keer staat het valideren van de input in de opdracht
        # /#RantOpHetCommentaarDatTelkensBijDeOpdrachtStaat
        if inp.isdigit():
            inp = int(inp)

            print('\n'.join(map(str, pyramid(inp, False))))
            print('')
            print('\n'.join(map(str, pyramid(inp, True))))

            break
        else:
            print("Helaas geen getal!. Probeer opnieuw!")
            continue


if __name__ == "__main__":
    main()
