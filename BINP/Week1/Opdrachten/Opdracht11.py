__author__ = 'Owain'

valueMales = input("How many males are their in class?")
valueFemales = input("How many females are their in class?")

totalPeople = int(valueFemales) + int(valueMales)

percentage = float((int(totalPeople) / 100))

print("{} {}".format("Percentage of males:", str((int(valueMales) / totalPeople) * 100)))
print("{} {}".format("Percentage of females:", str((int(valueFemales) / totalPeople) * 100)))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
