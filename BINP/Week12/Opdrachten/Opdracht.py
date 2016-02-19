__author__ = 'Owain'


def strip_special_chars(word: str) -> str:
    return ''.join([i for i in word if i.isalpha()]).lower()


def get_data(filename: str, mode: str) -> list:
    li = []

    with open(filename, mode) as f:
        for line in f:
            for word in line.split():
                li.append(strip_special_chars(word).lower())

    return li


def process_data(data: list) -> dict:
    word_dict = {}

    for i in data:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    return word_dict


def main() -> None:
    print(process_data(get_data('tekst.txt', 'r')))


if __name__ == '__main__':
    main()
