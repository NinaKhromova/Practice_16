class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return f"Клиент: \"{self.name}\". Баланс: {self.balance}."


user = User("Вася Пупкин", 100)
print(user.get_balance())
