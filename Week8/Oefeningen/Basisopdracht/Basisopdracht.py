import os

__author__ = 'Owain'


def open_file(name: str) -> str:
    with open(name) as fl:
        return fl.read()


def get_words(words: list, lenght: int) -> list:
    output = []

    for word in words:
        if len(word) == int(lenght):
            output.append(word)

    return output


def get_word(words: list, first_char: str) -> str:
    for word in words:
        if word[0] == first_char:
            return word


def write_to_file(word: str, file: str) -> None:
    with open(file, 'w') as f:
        print(word, file=f)


def main() -> None:
    words = open_file(os.path.dirname(os.path.abspath(__file__)) + "/woordenlijst.txt").split()

    input("Neem een woord in gedachten uit het bestand \"woordenlijst.txt\" en druk op [Enter]")

    while True:
        inp = input("Hoeveel letters heeft het woord?\n")

        if inp.isdigit():
            break

        print("Dit is geen geldige invoer. Probeer opnieuw!")

    words = get_words(words, inp)

    print("Dan is het één van de volgende woorden:")
    print('\n'.join(map(str, words)))

    while True:
        inp = input("Met welke letter begint het woord? \n")

        if inp.isalpha() and len(inp) == 1:
            write_to_file(get_word(words, inp), os.path.dirname(os.path.abspath(__file__)) + "/woord.txt")
            print("Open het bestand \"woord.txt\". Daarin staat het woord dat je in gedachten hebt.")
            break

        print("Dit is geen geldige invoer. Probeer opnieuw!")


if __name__ == "__main__":
    main()
