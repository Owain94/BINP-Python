from timeit import timeit
from re import sub, compile
from string import ascii_letters

__author__ = 'Owain'


def stripchars1(val: str) -> str:
    return ''.join([i for i in val if i.isalpha()]).lower()


def stripchars2(val: str) -> str:
    regex = compile('[^a-zA-Z]')
    return regex.sub('', val)


def stripchars3(val: str) -> bool:
    return ''.join(filter(lambda c: c.isalpha(), val))


def stripchars4(validChars):
    vc = set(validChars)
    def filter(s):
        return ''.join(ch for ch in s if ch in vc)
    return filter


def stripchars5(val: str) -> str:
    return ''.join([i for i in val if i in ascii_letters]).lower()


def test1() -> None:
    for i in range(5):
        stripchars1("<>TEST<>")
        stripchars1("!@#$%^&*()test!@#$%^&*()")


def test2() -> None:
    for i in range(5):
        stripchars2("<>TEST<>")
        stripchars2("!@#$%^&*()test!@#$%^&*()")


def test3() -> None:
    for i in range(5):
        stripchars3("<>TEST<>")
        stripchars3("!@#$%^&*()test!@#$%^&*()")


def test4() -> None:
    for i in range(5):
        filterAlpha = stripchars4(ascii_letters)
        filterAlpha("<>TEST<>")
        filterAlpha("!@#$%^&*()test!@#$%^&*()")


def test5() -> None:
    for i in range(5):
        stripchars5("<>TEST<>")
        stripchars5("!@#$%^&*()test!@#$%^&*()")

if __name__ == "__main__":
    print(timeit("test1()", setup="from __main__ import test1"))
    print(timeit("test2()", setup="from __main__ import test2"))
    print(timeit("test3()", setup="from __main__ import test3"))
    print(timeit("test4()", setup="from __main__ import test4"))