from re import match
from timeit import timeit
__author__ = 'Owain'


def is_float1(val: str) -> bool:
    return not match("^\d+?\.\d+?$", val) is None


def is_float2(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_float3(val: str) -> bool:
    num = True
    for c in val:
        if c not in '+-.0123456789':
            num = False

    if num:
        return False

    if '.' in val:
        return True


def test1() -> None:
    for i in range(5):
        is_float1("1")
        is_float1("a")


def test2() -> None:
    for i in range(5):
        is_float2("1")
        is_float2("a")


def test3() -> None:
    for i in range(5):
        is_float3("1")
        is_float3("a")

if __name__ == "__main__":
    print(timeit("test1()", setup="from __main__ import test1"))
    print(timeit("test2()", setup="from __main__ import test2"))
    print(timeit("test3()", setup="from __main__ import test3"))
