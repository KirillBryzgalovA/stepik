'''
Длина объекта
    Напишите рекурсивную функцию get_length(obj), которая принимает на вход итерируемый объект (строку, список или кортеж) и выводит его длину. Кроме функции ничего писать не нужно.
'''


def get_length(obj):
    return 0 if not obj else 1 + get_length(obj[1:])


print(get_length([1, 2, 3, 5, 7]))
