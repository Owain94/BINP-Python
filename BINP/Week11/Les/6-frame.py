from os import path

__author__ = 'Owain'

frame_dict = {
    "TTT": "F|Phe",
    "TTC": "F|Phe",
    "TTA": "L|Leu",
    "TTG": "L|Leu",
    "TCT": "S|Ser",
    "TCC": "S|Ser",
    "TCA": "S|Ser",
    "TCG": "S|Ser",
    "TAT": "Y|Tyr",
    "TAC": "Y|Tyr",
    "TAA": "*|Stp",
    "TAG": "*|Stp",
    "TGT": "C|Cys",
    "TGC": "C|Cys",
    "TGA": "*|Stp",
    "TGG": "W|Trp",
    "CTT": "L|Leu",
    "CTC": "L|Leu",
    "CTA": "L|Leu",
    "CTG": "L|Leu",
    "CCT": "P|Pro",
    "CCC": "P|Pro",
    "CCA": "P|Pro",
    "CCG": "P|Pro",
    "CAT": "H|His",
    "CAC": "H|His",
    "CAA": "Q|Gln",
    "CAG": "Q|Gln",
    "CGT": "R|Arg",
    "CGC": "R|Arg",
    "CGA": "R|Arg",
    "CGG": "R|Arg",
    "ATT": "I|Ile",
    "ATC": "I|Ile",
    "ATA": "I|Ile",
    "ATG": "M|Met",
    "ACT": "T|Thr",
    "ACC": "T|Thr",
    "ACA": "T|Thr",
    "ACG": "T|Thr",
    "AAT": "N|Asn",
    "AAC": "N|Asn",
    "AAA": "K|Lys",
    "AAG": "K|Lys",
    "AGT": "S|Ser",
    "AGC": "S|Ser",
    "AGA": "R|Arg",
    "AGG": "R|Arg",
    "GTT": "V|Val",
    "GTC": "V|Val",
    "GTA": "V|Val",
    "GTG": "V|Val",
    "GCT": "A|Ala",
    "GCC": "A|Ala",
    "GCA": "A|Ala",
    "GCG": "A|Ala",
    "GAT": "D|Asp",
    "GAC": "D|Asp",
    "GAA": "E|Glu",
    "GAG": "E|Glu",
    "GGT": "G|Gly",
    "GGC": "G|Gly",
    "GGA": "G|Gly",
    "GGG": "G|Gly"
}


def get_data(filename: str, mode: str = 'r') -> list:
    li = []

    with open(filename, mode) as f:
        for line in f:
            li.append(line.strip())

    return li


def process_data(data: list) -> list:
    lst = []

    for i in data:
        count = 0
        for j in i:
            count += 1

            data = i[count:count + 3]

            if len(data) == 3:
                lst.append('{}|{}'.format(data, count))

    firt_half = lst[:int(len(lst) / 2)]
    second_half = lst[int(len(lst) / 2):]

    return [firt_half, second_half]


def get_formatted_string(data: list):
    for i in data:
        count = 0
        for j in i:
            if int(i[count].split('|')[1]) % 3 == 0:
                print('module == 0 -- {}'.format(i[count]))
            elif int(i[count].split('|')[1]) % 3 == 1:
                print('module == 1 -- {}'.format(i[count]))
            elif int(i[count].split('|')[1]) % 3 == 2:
                print('module == 2 -- {}'.format(i[count]))

            count += 1


def main() -> None:
    filename, output_mode = '', ''

    while True:
        filename = input('Voer bestandsnaam in:\n')

        if path.isfile(filename):
            break
        else:
            print('Het betand kon niet gevonden worden!')

    while True:
        output_mode = input('1. 1-lettercode frame\n'
                            '2. 3-lettercode frame\n\n'
                            'Wat wil je zien? [1-2]\n')

        if output_mode in '12' and len(output_mode):
            break
        else:
            print('Dit is geen geldige invoer probeer opnieuw!')

    get_formatted_string(
        process_data(
            get_data(filename)
        )
    )


if __name__ == '__main__':
    main()
