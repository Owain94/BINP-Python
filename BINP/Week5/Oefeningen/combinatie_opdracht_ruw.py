from random import randint
print('Ik ga tien dobbelstenen gooien en de uitkomsten bij elkaar optellen.')
print('Ik hoop dat de uitkomst 37 is.')
d1 = randint(1,6)
d2 = randint(1,6)
d3 = randint(1,6)
d4 = randint(1,6)
d5 = randint(1,6)
d6 = randint(1,6)
d7 = randint(1,6)
d8 = randint(1,6)
d9 = randint(1,6)
d10 = randint(1,6)
uitkomst = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
print('Ik heb', uitkomst, 'gegooid.')
if uitkomst == 37:
    print('Het is gelukt!')
else:
    print('Het is niet gelukt.')
