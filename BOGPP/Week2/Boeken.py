from ast import literal_eval


class Book:
    def __init__(self, title: str, author: str, amount_of_pages: int,
                 status: bool = True) -> None:
        self.title = title
        self.author = author
        self.amount_of_pages = amount_of_pages
        self.code = self.book_code()
        self.status = status

    def __str__(self) -> str:
        return "Titel: {}\nAuteur: {}\nStatus: {}\nPagina's: {}\nCode: {}" \
            .format(self.title, self.author,
                    {True: "Beschikbaar",
                     False: "Niet beschrikbaar"}[self.status],
                    self.amount_of_pages, self.code)

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title
        self.code = self.book_code()

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str) -> None:
        self.author = author
        self.code = self.book_code()

    def get_status(self) -> bool:
        return self.status

    def set_status(self, status: bool) -> None:
        self.status = status

    def get_amount_of_pages(self) -> int:
        return self.amount_of_pages

    def set_amount_of_pages(self, amount_of_pages: int) -> None:
        self.amount_of_pages = amount_of_pages

    def get_book_code(self) -> str:
        return self.code

    def book_code(self):
        return (self.author.split(" ")[-1][:2] + self.title[:2]).upper()


def average_pages(books: list) -> int:
    total_pages = 0

    for book in books:
        total_pages += book.get_amount_of_pages()

    return round(total_pages / len(books))


def get_book_list(file: str) -> str:
    with open(file) as f:
        return f.read()


def resolve_book_data(data: str) -> list:
    books = []
    for line in data.split('\n'):
        book_data = line.split('|')

        if book_data[2].isdigit():
            books.append(Book(book_data[0],
                              book_data[1],
                              literal_eval(book_data[2])))

    return books


def main() -> None:

    books = resolve_book_data(get_book_list('Boeken.txt'))
    for book in books:
        print("{}\n".format(book))


if __name__ == '__main__':
    main()
