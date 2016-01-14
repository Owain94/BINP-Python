from re import compile


def stripchars(val: str) -> str:
    regex = compile('[^a-zA-Z]')
    return regex.sub('', val)


def main():
    for i in range(1001):
        stripchars("<>TEST<>")

if __name__ == "__main__":
    main()