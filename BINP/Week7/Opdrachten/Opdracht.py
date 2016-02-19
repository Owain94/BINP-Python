from os.path import exists

__author__ = 'Owain'

answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C',
           'A', 'D', 'C', 'B', 'B', 'D', 'A']


def check_file(name: str) -> bool:
    return exists(name)


def filer_input(f_in):
    return ''.join([i for i in f_in if not i.isdigit() and i != "."]).strip()


def read_file(r_file: str) -> list:
    with open(r_file, "r") as r_ins:
        r_list = []

        [r_list.append(filer_input(r_line)) for r_line in r_ins]

        r_ins.close()

    return r_list


def check_answers(c_check: list) -> list:
    c_list = []
    c_count = 1
    for c_i, c_j in zip(c_check, answers):
        if c_j.lower() != c_i.lower():
            c_list.append(c_count)

        c_count += 1

    return c_list


def get_score(g_list: list) -> str:
    if len(g_list) == 0:
        return "De student heeft de toets gehaald met " \
               "een perfect score van {}/{}!".format(
                len(answers), len(answers), len(answers),
                ', '.join(str(c) for c in g_list))
    else:
        return "De student heeft de toets {}gehaald!\nScore: {}/{} \n" \
               "Deze vragen waren verkeerd beantwoord: {}" \
            .format(['', 'NIET '][len(g_list) > 5],
                    len(answers) - len(g_list), len(answers),
                    ', '.join(str(c) for c in g_list))


def main() -> None:
    while True:
        file = input("Geef de naam van het bestand met de antwoorden:\n")

        if check_file(file):
            break
        else:
            print("Het bestand '{}' bestaat niet".format(file))

    print(get_score(check_answers(read_file(file))))


if __name__ == '__main__':
    main()
