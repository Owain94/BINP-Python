from re import finditer
from os.path import exists

__author__ = 'Owain'

enzymes = [
    {
        'abbrev': 'EcoRI',
        'full': 'Escherichia coli',
        'sequence': 'GAATTC',
        'offset': 1
    },
    {
        'abbrev': 'EcoRII',
        'full': 'Escherichia coli',
        'sequence': 'CCWGG',
        'offset': 0
    },
    {
        'abbrev': 'BamHI',
        'full': 'Bacillus amyloliquefaciens',
        'sequence': 'GGATCC',
        'offset': 1
    },
    {
        'abbrev': 'HindIII',
        'full': 'Haemophilus influenzae',
        'sequence': 'AAGCTT',
        'offset': 1
    },
    {
        'abbrev': 'NotI',
        'full': 'Nocardia otitidis',
        'sequence': 'GCGGCCGC',
        'offset': 2
    }
]


def is_numeric(value: str) -> bool:
    return value.isdigit()


def list_enzyms() -> str:
    string= ""
    for enzyme in enzymes:
        string += ("{}) {} ({})\n".format(enzymes.index(enzyme) + 1,
                                          enzyme["full"], enzyme["abbrev"]))

    return string


def check_file(name: str) -> bool:
    return exists(name)


def open_file(name: str) -> str:
    with open(name) as fl:
        return fl.read()


def check_enzym(sequence: str, sub: str, offset: int, inverse: bool = False)\
        -> list:
    value = []

    if not inverse:
        sequence = sequence.upper()
    else:
        sequence = sequence.upper()[::-1]

    for m in finditer(sub, sequence):
        value.append({m.start(), m.end(), m.start() + offset})

    return value


def result(results: list) -> list:
    string = []

    if not len(results) == 0:
        for i in results:
            i = list(i)

            string.append("Enzym gevonden op index {} tot {}, Dit enzym knipt "
                          "de sequentie na positie {}."
                          .format(i[2], i[1], i[0]))
    else:
        string.append("Dit enzym kon niet worden gevonden")

    return string


def main() -> None:
    while True:
        file = input("Geef de naam van het bestand met de DNA-sequentie:\n")

        if check_file(file):
            break
        else:
            print("Het bestand '{}' bestaat niet".format(file))

    print(list_enzyms())

    while True:
        val = input("Kies een enzym:\n")

        if is_numeric(val):
            inp = int(val)
            if inp in range(1, 6):
                break

        print("Dit is geen geldige invoer! probeer opnieuw!")

    print("{0}".format("\n".join(str(i) for i in result(
        check_enzym(open_file(file), enzymes[inp - 1]['sequence'],
                    enzymes[inp - 1]['offset'])))))

if __name__ == "__main__":
    main()
