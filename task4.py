#
def Srznach(num):
    if not num:
        return 0

    return sum(num) / len(num)

numb_list = list(map(int, input("Для ср. знач. ").split()))
print(f"Среднее значение: {Srznach(numb_list)}")

#Написать функцию, которая принимает список строк и возвращает словарь, где ключи — это длины строк, а значения — списки строк соответствующей длины.

def DictList(list_str):
    dict_len = {}

    for str in list_str:
        length = len(str)

        if length not in dict_len:
            dict_len[length] = []

        dict_len[length].append(str)

    return dict_len

str_list = list(map(str, input("Для словаря: ").split()))
print(f"словарь: {DictList(str_list)}")