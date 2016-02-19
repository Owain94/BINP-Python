__author__ = 'Owain'

value = input("What the total amount of land in square feet? ")

value = int(value) / 43560

print("{} {}".format("The total amount of acres is:", str("{0:.5f}".format(value)).replace('.', ',')))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
