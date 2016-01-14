from random import randint

__author__ = 'Owain van Brakel'
__version__ = "1"
__maintainer__ = "Owain van Brakel"
__email__ = "s1094204@student.hsleiden.nl"
__status__ = "Development"
__date__ = "7 Oct 2015"


def get_input(g_question: str, g_error="", g_type=-1, g_below=-1) -> str:
    """
        Vraag de gebruiker naar input en valideer deze.

        keyword arguments:
        g_question -- De vraag die er gesteld moet worden
        g_error -- De error die weergegeven moet worden als de validatie een error geeft
        g_type -- Type validatie (-1: geen, 1: numeriek, 2: numeriek maar kleiner dan g_below, 3: hl)
        g_below -- Kijk g_type
    """
    if g_type == 1 or g_type == 2:
        while True:
            g_value = input(g_question + "\n")
            if g_type == 1:
                if validate_input(g_value, "123456789"):
                    return g_value
            else:
                if validate_input(g_value, "123456789", g_below):
                    return g_value

            print(g_error)
            continue
    elif g_type == 3:
        while True:
            g_value = input(g_question + "\n")
            if validate_input(g_value, "hl"):
                return g_value

            print(g_error)
            continue
    else:
        return input(g_question + "\n")


def validate_input(v_value: str, v_seq: str, v_below=-1) -> bool:
    """
        Valideer of een string voldoet aan een aangegeven sequentie

        keyword arguments:
        v_value -- String om te valideren
        v_seq -- Sequentie waaraan v_value moet voldoen
        v_below -- Kijk of de waarde van de gevalideerde string onder deze waarde is
    """
    v_num = True
    for v_c in v_value:
        if v_c not in v_seq:
            v_num = False

    if v_below != -1:
        if v_num:
            return int(v_value) < v_below
        else:
            return False

    return v_num


def double_random(d_low: int, d_high: int) -> tuple:
    """
        Maak twee getalen aan dat tussen de twee meegegeven waardes in zitten en niet gelijk zijn aan elkaar


        keyword arguments:
        d_low -- Laagst mogelijke getal
        d_high -- Hoogst mogelijke getal
    """
    while True:
        d_rnd = random_number(d_low, d_high), random_number(d_low, d_high)
        if d_rnd[0] != d_rnd[1]:
            return d_rnd


def random_number(r_low: int, r_high: int) -> int:
    """
        Maak een getal aan dat tussen de twee meegegeven waardes in zit

        keyword arguments:
        r_low -- Laagst mogelijke getal
        r_high -- Hoogst mogelijke getal
    """
    return randint(r_low, r_high)


def guess_number(g_number: int, g_answer: int, g_player: str) -> tuple:
    """
        2 cijfers vergelijken

        keyword arguments:
        g_number -- Ingegeven nummer
        g_answer -- Antwoord
        g_player -- Naam van de huidige speler
    """
    return g_number == g_answer, g_player, g_number


def highest_number(h_number_1: int, h_number_2: int) -> tuple:
    """
        2 cijfers vergelijken

        keyword arguments:
        h_number_1 -- Nummer 1
        h_number_2 -- Nummer 2
    """
    return h_number_1 == h_number_2, h_number_1 < h_number_2, h_number_1, h_number_2


def lower_or_higher(l_number_1: int, l_number_2: int, l_answer: str) -> tuple:
    """
        Kijk of nummer 1 hoger / lager is dan getal 2

        keyword arguments:
        l_number_1 -- Nummer 1
        l_number_2 -- Nummer 2
        l_answer -- hoger / lager
    """
    if l_answer == "l":
        return l_number_1 > l_number_2, l_number_1, l_number_2, "lager"
    else:
        return l_number_1 < l_number_2, l_number_1, l_number_2, "hoger"


def main() -> None:
    score = [0, 0]
    i = 2

    players = [get_input("Hoe heet de {}e speler?".format(i + 1)).lower().capitalize() for i in range(2)]

    while score[0] < 10 and score[1] < 10:
        print("\nWie raadt als eerste het getal onder de 10?")
        rnd = random_number(1, 9)
        while True:
            player = players[i % 2]
            formatted_string = "{} wat denk jij dat het getal is?".format(player)

            val = guess_number(
                int(get_input(formatted_string, "Dat is geen geldige invoer, probeer opnieuw!", 2, 10)),
                rnd,
                player
            )

            if val[0]:
                print("De winnaar is {} met het getal {}.\n".format(val[1], val[2]))
                score[i % 2] += val[2]

                i = 2

                break
            else:
                print("Helaas {}, {} is niet het juiste getal\n".format(val[1], val[2]))

            i += 1

        print("\nWie gooit met dobbelen het hoogste getal?")
        while True:
            val = highest_number(random_number(1, 6), random_number(1, 6))
            print("{} gooit een {}\n{} gooit een {}".format(players[0], val[2], players[1], val[3]))

            if not val[0]:
                print("De winnaar is {} met het getal {}".format(players[int(val[1])], val[int(val[1]) + 2]))
                score[int(val[1])] += val[int(val[1]) + 2]

                break
            else:
                print("Gelijke score! We gooien nog een keer.")

        print("\nWie is er beter in hoger lager?")
        for i in range(2):
            print("\nDe beurt is aan {}!".format(players[i]))
            for j in range(5):

                rnd = double_random(1, 20)
                formatted_string = "{}, wat denk jij, is het getal hierna hoger of lager dan {}? (h/l)"\
                    .format(players[i], rnd[0])

                val = lower_or_higher(
                    rnd[0],
                    rnd[1],
                    get_input(formatted_string, "Dat is geen geldige invoer, probeer opnieuw!", 3)
                )

                if val[0]:
                    print("{} is inderdaad {} dan {}\n".format(val[2], val[3], val[1]))
                    score[i] += 1
                else:
                    print("Helaas, {} is niet {} dan {}, je hebt het {} ronde(n) uitgehouden.\n"
                          .format(val[1], val[3], val[2], j))
                    break

    print("De uitslag:\n\n{} heeft {} punten\n{} heeft {} punten\n".format(players[0], score[0], players[1], score[1]))
    if score[0] == score[1]:
        print("Dat betekend dus dat het gelijk spel is geworden.")
    else:
        print("Dat betekend dus dat {} heeft gewonnen!".format(players[int(score[0] < score[1])]))


if __name__ == "__main__":
    main()
