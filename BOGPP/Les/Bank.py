class Rekening:

    def __init__(self, balance: int) -> None:
        self.balance = self.check_value(balance)

    def __str__(self) -> str:
        return "Balans: {.2f}".format(self.balance)

    def get_balance(self) -> int:
        return self.balance

    def set_balance(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount: any) -> None:
        self.balance -= self.check_value(amount)

    def deposit(self, amount: any) -> None:
        self.balance += self.check_value(amount)

    @staticmethod
    def check_value(amount) -> any:
        if not isinstance(amount, int) and not isinstance(amount, float):
            amount = 0
        return round(amount, 2)


def main()->None:

    rekeningen = [Rekening(10),
                  Rekening(20),
                  Rekening(30),
                  Rekening(40)]

    for rekening in rekeningen:
        print("{:.2f}".format(rekening.get_balance()))
        rekening.deposit(10)
        print("{:.2f}".format(rekening.get_balance()))
        rekening.deposit(10.50)
        print("{:.2f}".format(rekening.get_balance()))
        rekening.withdraw("ask")
        print("{:.2f}".format(rekening.get_balance()))
        print("\n")


if __name__ == '__main__':
    main()
