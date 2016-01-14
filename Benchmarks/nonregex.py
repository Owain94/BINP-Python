def stripchars(val: str) -> str:
    return ''.join([i for i in val if i.isalpha()]).lower()


def main():
    for i in range(1001):
        stripchars("<>TEST<>")

if __name__ == "__main__":
    main()