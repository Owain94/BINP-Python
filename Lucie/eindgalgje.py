""""
Scriptnaam: Galgje.py
Auteur: Lucie Pot
Datum: 7 december 2015
Versie: 1

"""
from random import choice
from time import time
from string import ascii_lowercase

"Deze functie zorgt ervoor dat als deze functie wordt aangeroepen"
"Telkens een bestand wordt geladen."


def bestand_laden(bestand):
    file = open(bestand, 'r', encoding='latin1')
    inhoud = file.read().splitlines()
    file.close()
    return inhoud


"Optie1: woord toevoegen.Deze functie voegt een woord toe aan de lijst."
"De functie stript en sorteert o.a. de toegevoegde woorden."


def woord_toevoegen():
    woordenlijst = bestand_laden('woorden.txt')
    woord = input('Voeg een woord toe: ')
    woordstring = ""
    for i in woord:
        if i.isalpha():
            woordstring += i.lower()
    if len(woordstring) < 3 or len(woordstring) > 38:
        print('Het woord mag niet korter zijn dan 3 letters en niet langer'
              'dan 38 letters')
    elif woordstring in woordenlijst:
        print('Dit woord komt al voor in de lijst')
    else:
        woordenlijst.append(woordstring)
        woordenlijst.sort()
        woordenlijst.sort(key=len)
        inhoud = open('woordenlijst.txt', 'w', encoding='latin1')
        for item in woordenlijst:
            inhoud.write('\n'.join(woordenlijst))
        print('Het woord:', woordstring, 'is toegevoegd.')
        inhoud.close()


"Optie2: spel spelen. Eerst wordt er een geheim woord gekozen."


def geheim_woord():
    woordenlijst = bestand_laden('woorden.txt')
    secret_woord = choice(woordenlijst)
    print(secret_woord)

    return secret_woord


def spel_spelen(s_guessed, s_wrong, s_word):
    s_guessed = []
    s_wrong = []
    pogingen = 9
    galg_pogingen = 0
    while pogingen > 0:
        out = ""
        for letter in s_word:
            if letter in s_guessed:
                out = out + letter
            else:
                out += "*"
        if out == s_word:
            break

        print(galg(galg_pogingen, out, s_guessed))

        # print("Raad het woord of letter:\n", out)
        print(pogingen, "kansen over")
        guess = input()
        if (guess in s_guessed or guess in s_wrong) and len(guess) == 1:
            print("Deze letter heeft u al geraden", guess)
        elif guess in s_word and len(guess) == 1:
            print("Goede gok")
            s_guessed.append(guess)
        elif guess == s_word:
            for letter in guess:
                if letter not in s_guessed:
                    s_guessed.append(letter)
        else:
            print("Foute gok")
            pogingen -= 1
            galg_pogingen += 1
            s_wrong.append(guess)
            s_guessed.append(letter)
        print()
    if pogingen:
        print("U heeft het woord", s_word, "geraden\n")
    else:
        print("Helaas, u heeft verloren.Het woord was:", s_word, '\n')
    return s_word


"Deze functie zorgt dat de galg wordt uitgelezen."


def galg_uitlezen():
    galg_text = bestand_laden('figuren.txt')
    schone_galg = []
    for regel in galg_text:
        tmp = ''.join(regel[3:])
        tmp = tmp.split(';')
        schone_galg.append(tmp)
    return schone_galg


"Deze functie zorgt dat de goede galg wordt geprint bij het goede"
"aantal pogingen."


def galg(g_pogingen, g_woord, g_guessed):
    out = ''
    letters = []
    if g_pogingen > 9:
        g_pogingen = 9

    i_galg = galg_uitlezen()

    for i in ascii_lowercase:
        if i in g_guessed:
            letters.append(i)
        else:
            letters.append('*')

    out += 'Galgje:' + (' ' * 50) + 'Geraden letters\n'
    out += i_galg[g_pogingen][0] + (' ' * 50) + ' '.join(letters[0:9]) + '\n'
    out += i_galg[g_pogingen][1] + '\n'
    out += i_galg[g_pogingen][2] + (' ' * 50) + ' '.join(letters[9:18]) + '\n'
    out += i_galg[g_pogingen][3] + '\n'
    out += i_galg[g_pogingen][4] + (' ' * 52) + ' '.join(
            letters[18:26]) + '\n'
    out += i_galg[g_pogingen][5] + '\n'
    out += (' ' * 25) + 'Te raden woord\n'
    out += (' ' * 30) + g_woord
    return out


"Met deze functie kun je de rankinglijst openen en bekijken."


def ranking_bekijken(r_naam_player):
    rankinglijst = bestand_laden('ranking.txt')
    rankinglijst.append(r_naam_player)
    rankinglijst.sort()
    inhoud = open('ranking.txt', 'w', encoding='latin1')
    for item in rankinglijst:
        item = item.split(";")
        inhoud.write('\n'.join(rankinglijst))
    inhoud.close()
    print(rankinglijst)


"Deze functie berekent de score van de speler."


def bereken_score(b_secret_woord, b_pogingen, b_tijdsduur):
    score = 10000 * (len(b_secret_woord) / (b_tijdsduur * b_pogingen + 1))
    return int(score)


"Dit is de main functie er roept alle functies aan."


def main():
    naam_player = input('Wat is je naam? ')
    while True:
        print('Selecteer een van de volgende opties:\n1) Een woord toevoegen'
              '\n2) Het spel spelen\n3) De ranking bekijken\n4) Stoppen')
        selection = input('')
        try:
            selection = int(selection)
        except ValueError:
            print('Geen geldige optie geselecteerd')
            continue
        if selection not in range(1, 5):
            print('Geen geldige optie geselecteerd')
            continue
        if selection == 1:
            woord_toevoegen()
            print('Woord toevoegen')
        if selection == 2:
            pogingen = 0
            woord = geheim_woord()
            guessed = []
            wrong = []
            begin = time()
            spel_spelen(guessed, wrong, woord)
            # print("U heeft", bereken_score(secret_woord, pogingen,
            # tijdsduur),
            #      "punten gescoord.")
            #          print(interface(pogingen, galg))
        if selection == 3:
            print('Ranking bekijken')
            ranking_bekijken(naam_player)
        if selection == 4:
            print('Bedankt voor het spelen')
            exit()


main()
