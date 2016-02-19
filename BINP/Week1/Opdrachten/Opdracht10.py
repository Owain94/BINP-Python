__author__ = 'Owain'

# vars
sugar = 1.5
butter = 1
flour = 2.75

# amount of cookies you can make of the above ingredients
amount = 48

# get amount for one cookie
sugar /= amount
butter /= amount
flour /= amount

amount_to_make = 0


# verify the input
def verify_input(value):
    # check if the input is an int
    try:
        int(value)
    # catch the exception if the input isn't an int
    except ValueError:
        print("Oops! That is not a number. Try again...")
        return -1
    # the input is an int!
    else:
        # check if the int is negative
        if int(value) < 0:
            # if the int is negative continue the loop
            print("Oops! That is not a positive number. Try again...")
            return -1
        # if the int is positive return it
        else:
            return value


while True:
    # save the input
    val = verify_input(input("How many cookies do you want to make?\n"))

    # verify the return value
    if val != -1:
        # the value is valid
        amount_to_make = val
        break
    else:
        # continue with the loop
        continue

print("\nYou'll need\n")

# format the output
print("{} {}".format("{0:.2f}".format(sugar * int(amount_to_make)).replace('.', ','), "cups of sugar"))
print("{} {}".format("{0:.2f}".format(butter * int(amount_to_make)).replace('.', ','), "cups of butter"))
print("{} {}".format("{0:.2f}".format(flour * int(amount_to_make)).replace('.', ','), "cups of flour"))

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
