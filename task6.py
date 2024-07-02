#Написать программу, которая запрашивает у пользователя ввод числа и
#обрабатывает возможное исключение при неверном вводе.
def CheckInt(num):
    try:
        answer = int(num)
        print(f"Вы ввели число: {answer}")

    except ValueError:
        print("Некорректный ввод")

    # else:
    #     print("Операция выполнена успешно.")

    # finally:
    #     print("Программа завершена.")


check = CheckInt(input("Введите число: "))

#Написать функцию, которая делит два числа и обрабатывает исключение
#деления на ноль.

def DivisionZero():
    try:
        x = int(input("Введите числитель: "))
        y = int(input("Введите знаменатель: "))
        gg = x / y
        print(f"Результат: {gg}", "\n")

    except ValueError:
        print("Ошибка: введено не числовое значение.", "\n")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль.", "\n")

    else:
        print("Операция выполнена успешно.", "\n")

    finally:
        print("Программа завершена.", "\n")

DivisionZero()

#Написать программу, которая считывает содержимое файла и обрабатывает
# возможные исключения, такие как FileNotFoundError и PermissionError. (если
# есть трудности, прочтите тему контекстных менеджеров и можете
# возвращаться)

def FileRead():
    try:
        with open('123.txt', 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("Файл не найден", "\n")

    except PermissionError:
        print("Нет доступа", "\n")

    else:
        print("Операция выполнена успешно.", "\n")

    finally:
        print("Программа завершена.")

FileRead()