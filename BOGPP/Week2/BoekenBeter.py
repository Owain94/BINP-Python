from ast import literal_eval
from xml.dom import minidom


class Book:
    def __init__(self, title: str, author: str, amount_of_pages: int,
                 status: bool = True) -> None:
        self._title = title
        self._author = author
        self._amount_of_pages = amount_of_pages
        self._code = self.book_code()
        self._status = status

    def __str__(self) -> str:
        return "Titel: {}\nAuteur: {}\nStatus: {}\nPagina's: {}\nCode: {}" \
            .format(self.title, self.author,
                    {True: "Beschikbaar",
                     False: "Niet beschrikbaar"}[self.status],
                    self.amount_of_pages, self.code)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value
        self._code = self.book_code()

    @title.deleter
    def title(self) -> None:
        del self._title

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value
        self._code = self.book_code()

    @author.deleter
    def author(self) -> None:
        del self._author

    @property
    def status(self) -> bool:
        return self._status

    @status.setter
    def status(self, value: bool) -> None:
        self._status = value

    @status.deleter
    def status(self) -> None:
        del self._status

    @property
    def amount_of_pages(self) -> int:
        return self._amount_of_pages

    @amount_of_pages.setter
    def amount_of_pages(self, value: int) -> None:
        self._amount_of_pages = value

    @amount_of_pages.deleter
    def amount_of_pages(self) -> None:
        del self._amount_of_pages

    @property
    def code(self) -> str:
        return self._code

    @code.deleter
    def code(self) -> None:
        del self._amount_of_pages

    def book_code(self) -> str:
        return (self.author.split(" ")[-1][:2] + self.title[:2]).upper()


def average_pages(books: list) -> int:
    total_pages = 0

    for book in books:
        total_pages += book.amount_of_pages

    return round(total_pages / len(books))


def parse_book_list(file: str) -> list:
    book_list = []

    doc = minidom.parse(file)
    books = doc.getElementsByTagName("book")
    for book in books:
        title = book.getElementsByTagName("title")[0].firstChild.data
        author = book.getElementsByTagName("author")[0].firstChild.data
        pages = book.getElementsByTagName("pages")[0].firstChild.data

        if pages.isdigit():
            book_list.append(Book(title, author, literal_eval(pages)))

    return book_list


def main() -> None:
    books = parse_book_list('Boeken.xml')
    for book in books:
        print("{}\n".format(book))

    print("Average amount of pages: {}".format(average_pages(books)))


if __name__ == '__main__':
    main()
