#Написать программу, которая использует while цикл для подсчета суммы чисел от 1 до 100.

i = 1
isum = 0

while i <= 100:
    isum += i
    i += 1

print(f"сумма чисел от 1 до 100: {isum}")

#Написать функцию, которая принимает список чисел и возвращает два списка отсортированных по четному и нечетному числу

n = list(map(int, input("Сортировка по чот, нечет: ").split()))
chot = []
nechot = []

for number in n:
    if number % 2:
        nechot.append(number)
    else:
        chot.append(number)

print(f"четные {sorted(chot)}")
print(f"нечетные {sorted(nechot)}")

#Написать программу, которая генерирует все простые числа в диапазоне от 1 до 100 с использованием цикла for.
simple_list = []
def IsSimple(num) -> bool:
    if num <= 1:
        return False
    
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            return False
    
    return True

for i in range(1, 100 + 1):
    if (IsSimple(i)):
        simple_list.append(i)

print(f"простые числа: {simple_list}")

#Написать программу, которая использует цикл while для подсчета факториала числа, введенного пользователем.
        
fact_num = int(input("Факториал: "))

factorial = 1
i = 1

while i <= fact_num:
    factorial *= i
    i += 1

print(f"факт. числа {fact_num} = {factorial}")

#Написать генератор, который возвращает бесконечную последовательность чисел Фибоначчи.

def Fibonachi(n):
    a, b = 0, 1
    i = 1
    while i <= n:
        yield a
        a, b = b, a + b
        i += 1

print(f"10 чисел фибоначи: {list(Fibonachi(10))}")

