from timeit import timeit

__author__ = 'Owain'


def is_int1(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


def is_int2(val: str) -> bool:
    return val.isdigit()


def is_int3(val: str) -> bool:
    num = True
    for c in val:
        if c not in '+-.0123456789':
            num = False

    if num:
        if '.' not in val:
            return True

    return False


def test1() -> None:
    for i in range(5):
        is_int1("1")
        is_int1("a")


def test2() -> None:
    for i in range(5):
        is_int2("1")
        is_int2("a")


def test3() -> None:
    for i in range(5):
        is_int2("1")
        is_int2("a")

if __name__ == "__main__":
    print(timeit("test1()", setup="from __main__ import test1"))
    print(timeit("test2()", setup="from __main__ import test2"))
    print(timeit("test3()", setup="from __main__ import test3"))
