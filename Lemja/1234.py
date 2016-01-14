running = True

while running:
    inp = input('Wat wil je doen? [1/2/3/4]\n')

    if inp in '1234' and len(inp) == 1:

        print('Hier ga ik allemaal gekke dingen doen')

        running = False
    else:
        print('Dit is geen geldige invoer, probeer opnieuw!')