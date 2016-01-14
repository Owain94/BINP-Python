def main() -> None:
    li = []

    for i in range(1, 6):
        val = input("vul de {}e naam in:\n".format(i))

        li.append(val)

    with open('namenlijst.txt', 'w') as file:
        file.write('\n'.join(li))

    with open('namenlijst.txt', 'r') as file:
        print(file.read())

if __name__ == "__main__":
    main()

