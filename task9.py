import time
from threading import Thread
from typing import List

#Написать программу, которая открывает файл для чтения, читает его
#содержимое и закрывает файл автоматически с использованием with.
with open('123.txt', 'r') as file:
    content = file.read()
    print(content)

# Создайте классы Car, Driver
# Car, свойства: mileage (пробег), is_turned_on, driver
# Driver, наследуется от класса Person, опишите на своё усмотрение
# Далее, создайте контекстный менеджер, который будет принимать в себя
# аргументы car, driver, и при инициализации контекстного менеджера, будет
# включать двигатель машины, и каждую секунду пока двигатель активен,
# добавлять +1 к mileage, и когда мы выходим из контекста, двигатель глушился и
# реализуйте валидацию ситуации, когда пользователь пытается завести уже
# заведенную машину.
# Дополнительно: добавьте валидацию, что машиной может управлять только
# тот человек, чья это машина, и возвращать ошибку, если машиной начал
# управлять не собственник машины. Затем, поменяйте свойство driver, на drivers,
# и реализуйте логику чтобы собственников могло быть несколько.
# Супер-дополнительно: реализуйте метод, с помощью которого можно будет
# узнать каким т/c в данный момент управляет водитель, и какими машинами
# владеет

class Person:
    def __init__(self, name):
        self.name = name

    def Name(self):
        return self.name


class Driver(Person):
    def __init__(self, name, lisense):
        super().__init__(name)
        self.lisense = lisense


class Car:
    def __init__(self, mileage, is_turned_on, drivers):
        self.mileage = mileage
        self.is_turned_on = is_turned_on
        self.driver = drivers 

    def Start(self):
        self.is_turned_on = True

    def Stop(self):
        self.is_turned_on = False


class CarContextManager:
    def __init__(self, car: Car, driver: Driver):
        self.car = car
        self.driver = driver
        self.thread = None
        self.running = False

    def __enter__(self):
        if self.car.is_turned_on:
            raise Exception("Ошибка: Машина уже заведена.")

        if self.driver not in self.car.driver:
            raise Exception("Ошибка: Водитель не является владельцем машины.")

        self.car.Start()
        self.running = True
        self.thread = Thread(target=self._run)
        self.thread.start()

    def _run(self):
        while self.running:
            time.sleep(1)
            self.car.mileage += 1
            print(f"Пробег: {self.car.mileage}")

    def __exit__(self, exc_type, exc_value, traceback):
        self.running = False
        self.thread.join()
        self.car.Stop()


driver1 = Driver("Леша", "12345")
driver2 = Driver("Вова", "54321")
driver3 = Driver("sdadsa", '123213342143124312')
car1 = Car(5000, False, [driver1, driver2])
car2 = Car(3500, True, [driver1, driver2, driver3])

try:
    with CarContextManager(car1, driver1): #тест водил
        time.sleep(5)

    with CarContextManager(car1, driver2):
        time.sleep(5)

    with CarContextManager(car1, driver3):
        time.sleep(5)

    with CarContextManager(car2, driver3): #машина уже заведена
        time.sleep(5)

except Exception as e:
    print(e)

