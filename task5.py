#Создать класс Car с атрибутами made_by, model и методом display_info, который выводит информацию о машине.
class Car:
    def __init__(self, made_by, model):
        self.made_by = made_by
        self.model = model

    def DisplayInfo(self):
        print(f"Марка: {self.made_by}, Модель: {self.model}")

car1 = Car("Lada", "Vesta")
car2 = Car("Kia", "Picanto")

car1.DisplayInfo()
car2.DisplayInfo()

#Создать класс BankAccount с атрибутами balance и методами deposit,
# withdraw, и get_balance. Реализовать контроль за достаточностью средств при снятии.

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Депозит: {amount}. Новый баланс: {self.__balance}")

        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств для снятия.")

        elif amount <= 0:
            print("Сумма снятия должна быть положительной.")

        else:
            self.__balance -= amount
            print(f"Снятие: {amount}. Новый баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
print(f"Баланс: {account.get_balance()}", "\n")

account.deposit(50)
print(f"Баланс: {account.get_balance()}", "\n")

account.withdraw(30)
print(f"Баланс: {account.get_balance()}", "\n")

account.withdraw(200)  
print(f"Баланс: {account.get_balance()}", "\n")
