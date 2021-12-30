class Human:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    status = "Не определён"

    def get_info(self):
        return f"{self.name}, г. {self.location}, статус \"{self.status}\"."


class Mentor(Human):
    status = "Наставник"


class Student(Human):
    status = "Ученик"


list = {
    Mentor("Игорь Петрович", "Москва"),
    Mentor("Василий Иваныч", "Новосибирск"),
    Student("Василич", "Краснодар"),
    Human("Какой-то левый чел", "Ростов"),
}

for human in list:
    print(human.get_info())
