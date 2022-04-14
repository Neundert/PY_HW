class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum(self._income.values())

a = Position('ivan','ivanov','worker', 10000, 5000)
print(a.get_full_name())
print(a.get_total_income())