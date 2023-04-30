'''
Слияние словарей 🌶️
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.
'''


def merge(values):  # values - это список словарей
    dict_merge = {}
    for dictionary in values:
        for key, value in dictionary.items():
            if key not in dict_merge:
                dict_merge[key] = {value}
            else:
                dict_merge[key].add(value)
    return dict_merge


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)
