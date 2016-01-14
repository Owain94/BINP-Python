from re import match

__author__ = 'Owain'


def is_numeric(value):
    return value.isdigit()


def is_positive(value):
    return float(value) > 0


def is_float(val):
    return not match("^\d+?\.\d+?$", val) is None


def only_letters(value):
    return str(value).replace(' ', '').isalpha()


def single_character(value):
    if len(value) > 1:
        return False
    else:
        return True

# Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.
