'''
Загадка от Жака Фреско 🌶️

Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.
'''


with open('goats.txt', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as file2:
    line = file.readline()
    dictionary = dict()
    while line != "GOATS":
        line = file.readline().strip()
        if line != "GOATS":
            dictionary[line] = 0
    total = 0
    for line in file:
        line = line.strip()
        dictionary[line] = dictionary.get(line, 0) + 1
        total += 1

    result = list(filter(lambda item: dictionary[item] * 100 > total * 7, dictionary))

    result.sort()
    for item in result:
        file2.write(item + '\n')
