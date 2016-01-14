running = True

while running:
    try:
        value = input('Voer een getal in:\n')

        int(value)

        running = False
    except ValueError:
        print('{} is geen geldige invoer, probeer opnieuw!'.format(value))

print('Het ingegeven getal is: {}'.format(value))