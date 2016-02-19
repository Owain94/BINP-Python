from random import randint

__author__ = 'Mies'


def hl(h_naam_speler):  # Naam van de functie mag geen hoofdletters bevatten volgens PEP8!
    """
        Deze functie print een random getal tussen 1 en 20 en neemt een input.
        De gebruiker antwoordt "h" of "l", op basis van de gedachten van de gebruiker of het volgende getal hoger of
        lager is. Als het fout is stopt de functie en als er vijf punten behaald zijn ook.


    """
    h_getal_2 = randint(1, 20)
    for h_punten in range(0, 5):
        h_getal_1, h_getal_2 = h_getal_2, randint(1, 20)
        print("Het getal is:", h_getal_1)
        h_inp = input("%s, wat denk jij, is het getal hierna hoger of lager? (h/l)" % h_naam_speler)
        if h_getal_1 == h_getal_2:
            print("Het getal is even hoog. Je krijgt een punt!")
        elif (h_inp == "h" and h_getal_2 > h_getal_1) or (h_inp == "l" and h_getal_2 < h_getal_1):
            print("{}, dat klopt!".format(['Hoger', 'Lager'][h_inp == 'l']))
        else:
            print("Helaas, niet goed. Je hebt het {} ronden volgehouden. Het was getal {}".format(h_punten + 1,
                                                                                                  h_getal_2))
            break
    print("Het spel is afgelopen. Je hebt", h_punten + 1, "punten behaald!")
    return h_punten + 1


def gooi_afhandelen(g_speler1, g_speler2, g_random, g_score1):
    print(g_speler1 + " gooit een " + str(g_score1))
    print(g_speler2 + " gooit een " + str(g_random))

    if g_score1 == g_random:
        print("Gelijke score! We gooien nog een keer.")
        return True
    else:
        if g_score1 > g_random:
            print(g_speler1 + " heeft gewonnen!")
            return g_speler1, g_score1
        else:
            print(g_speler2 + " heeft gewonnen!")
            return g_speler2, g_random


def hoogste_gooit(h_speler1, h_speler2):
    h_draw, h_score1 = True, 0

    while h_draw:
        for h_i in range(1, 3):
            h_random = randint(1, 6)

            if h_i == 1:
                h_score1 = h_random
            else:
                h_value = gooi_afhandelen(h_speler1, h_speler2, h_random, h_score1)

                if h_value != True:
                    return h_value


def raden(r_speler1, r_speler2):
    r_winnaar = 0
    print('Wie raadt als eerste het getal onder de 10?')
    while r_winnaar == 0:
        r_antwoord1 = numeral_input(r_speler1 + ' wat denk jij dat het is?\n', True, True, 'Geen geldig getal',
                                    'Geen positief getal')
        r_antwoord2 = numeral_input(r_speler2 + ' wat denk jij dat het is?\n', True, True, 'Geen geldig getal',
                                    'Geen positief getal')
        r_randomNummer = randint(1, 10)
        if r_randomNummer == r_antwoord1:
            print('De winnaar is', r_speler1, 'met getal', str(r_randomNummer))
            r_winnaar = 1
        elif r_randomNummer == r_antwoord2:
            print('De winnaar is', r_speler2, 'met getal', str(r_randomNummer))
            r_winnaar = 2
    return r_winnaar, 5


def get_name(g_msg='Enter name:\n'):
    g_name = ''
    while len(g_name) < 1:
        g_name = input(g_msg)
    return g_name


def numeral_input(n_msg="Please enter a valid number.\n",
                  n_positive=False,
                  n_roundnumber=False,
                  n_errormsg="Can't convert to number, please try again. \n",
                  n_notposmes="Number is not more than zero, please try again."):
    while True:

        n_inputval = input(n_msg)

        try:
            if n_roundnumber:
                n_floatinput = int(n_inputval)
            else:
                n_floatinput = float(n_inputval)

            if n_positive and n_floatinput < 0:
                print(n_notposmes)
                continue

            return n_floatinput
        except ValueError:
            print(n_errormsg)
            continue


def get_length_longest_entry(g_array, g_field):
    g_longest = 0
    for g_entry in g_array:
        if len(g_entry[g_field]) > g_longest:
            g_longest = len(g_entry[g_field])
    return g_longest


def scoreboard(s_scores, s_players):
    s_longestname = get_length_longest_entry(s_scores, 'playername')
    s_longestgame = get_length_longest_entry(s_scores, 'game')

    print(s_longestname)


def main():
    # Get playername
    player1, player2 = get_name('Naam speler 1\n'), get_name('Naam speler 2\n')

    # Scores
    score_player1, score_player2 = 0, 0

    while score_player1 < 10 and score_player2 < 10:

        # Game 1
        winnaar, score = raden(player1, player2)
        if winnaar == 1:
            score_player1 += score
        else:
            score_player2 += score

        # Game 2
        winnaar, score = hoogste_gooit(player1, player2)

        if winnaar == player1:
            score_player1 += score
        else:
            score_player2 += score

        # Game 3
        score_player1, score_player2 = hl(player1) + score_player1, hl(player2) + score_player2

    # Scores
    print('Scores : \n{} : {} \n{} : {}'.format(player1, score_player1, player2, score_player2))


if __name__ == '__main__':
    main()
