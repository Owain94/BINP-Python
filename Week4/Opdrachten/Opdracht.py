__author__ = 'Owain'


def calc(val: int, increase: str) -> float:
    return float(val) + (float(val) * float(increase))


def format_input(val: int) -> str:
    return "0.{}".format(val)


def main() -> None:
    average_increase = 0
    days_multiply = 9
    begin_val = 0

    for i in range(0, 3):
        if i == 0:
            string = "Met hoeveel organismes wordt er begonnen?\n"
        elif i == 1:
            string = "Wat is het percentage van de dagelijkse groei?\n"
        else:
            string = "Hoeveel dagen wordt dit gekweekt?\n"

        while True:
            inp = input(string)

            if inp.isdigit():
                value = int(inp)

                if i == 0:
                    begin_val = value
                elif i == 1:
                    average_increase = value
                else:
                    days_multiply = value

                break

    average_increase = format_input(average_increase)

    for i in range(1, int(days_multiply)):
        begin_val = calc(begin_val, average_increase)

        print("Dag {}: populatie: {}".format(i, "{:.2f}".format(begin_val)))

if __name__ == "__main__":
    main()
