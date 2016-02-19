class Student:

    def __init__(self, student_nr: int, student_name: str,
                 student_residence: str, student_age: int) -> None:
        self.student_nr = student_nr
        self.age = student_age
        self.name = student_name
        self.residence = student_residence
        self.totalec = 0

    def __str__(self) -> str:
        return "Student nummer: {}\nNaam: {}\nLeeftijd: {}\n" \
               "Woonplaats: {}\nStudiepunten: {}"\
            .format(self.student_nr, self.name, self.age, self.residence,
                    self.totalec)

    def get_student_nr(self) -> int:
        return self.totalec

    def set_student_nr(self, student_nr) -> None:
        self.student_nr = student_nr

    def get_age(self) -> int:
        return self.age

    def set_age(self, new_age: int) -> None:
        self.age = new_age

    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_residence(self) -> str:
        return self.residence

    def set_residence(self, new_residence: str) -> None:
        self.residence = new_residence

    def get_total_ec(self) -> int:
        return self.totalec

    def set_total_ec(self, new_total_ec: int) -> None:
        self.totalec += new_total_ec


def main()->None:
    students = [Student(1, 'Mies', 'Den Haag', 12),
                Student(1, 'Harry', 'Den Haag', 42),
                Student(1, 'Gerrit', 'Den Haag', 32),
                Student(1, 'Zoe', 'Den Haag', 18)]

    total_age = 0

    print(students[0].student_nr)

    for student in students:
        total_age += student.get_age()

    average_age = total_age / len(students)

    print(average_age)
    print(students[0].get_total_ec())
    students[0].set_total_ec(60)
    print(students[0].get_total_ec())
    students[0].set_total_ec(60)
    print(students[0].get_total_ec())


if __name__ == '__main__':
    main()