#Создать список из нескольких чисел и строк, затем разделить его на два списка:
#один для чисел, другой для строк.
mix_list = [1, 2, 3, 'bababoy', "mlg123", "sania", 777, "qwerty"]
numbers_list = []
string_list = []

for item in mix_list:
    if isinstance(item, int):
        numbers_list.append(item)

    elif isinstance(item, str):
        string_list.append(item)

print(numbers_list)
print(string_list)

#Написать программу, которая подсчитывает количество уникальных слов в
# тексте, введенном пользователем. Вывести статистику по количеству
# уникальных слов и общее количество слов.

user_input = input().split()
total_words = len(user_input)
unique_words = len(set(user_input))

print("Общее количество слов: ", total_words)
print("Количество уникальных слов: ", unique_words)

#

