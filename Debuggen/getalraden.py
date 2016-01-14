
def hogerlager(h_onder, h_boven):
    """
    Deze functie krijgt een ondergrens en een bovengrens mee. Het getal
    dat de gebruiker in gedachten heeft moet zich ergens tussen deze grenzen
    bevinden. Aan de gebruiker wordt gevraagd of zijn getal lager is dan
    het middenpunt tussen de onder- en bovengrens. Afhankelijk van het
    antwoord wordt de onder- of bovengrens bijgesteld en teruggegeven.
    """
    grens = int(h_onder + ((h_boven-h_onder)/2))
    antw = input('Is het getal lager of gelijk aan ' + str(grens) + ' (j/n)?')
    if antw == 'j':
        h_boven = grens
    else:
        h_onder = grens
    return h_boven, h_onder


def main():
    """
    Dit programma raadt het getal dat de gebruiker in gedachten heeft. Dit
    doet het door steeds de grenzen bij te stellen waarbinnen het getal moet
    vallen.
    """
    ondergrens = 1
    bovengrens = 100
    print('Neem een getal in gedachten')
    print('Het mag niet lager zijn dan', ondergrens, 'en niet hoger dan', bovengrens)
    input('Als je een getal bedacht hebt, druk dan op [Enter]')
    teller = 0
    while bovengrens-ondergrens != 1:
        teller += 1
        bovengrens, ondergrens = hogerlager(ondergrens, bovengrens)
    print('Het getal is', bovengrens, '(in', teller, 'keer geraden).')

main()
