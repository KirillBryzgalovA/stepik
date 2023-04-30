'''
Лог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время выхода, где время указано в 2424-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка следования), которые были в сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в файле нет двух строк с одинаковым пользователем.

'''
import datetime

with open('logfile.txt', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as outputfile:
    for line in file:
        content = line.strip().replace(',', '').split(' ')
        time_input = content[2]
        time_output = content[3]

        t1 = datetime.timedelta(hours=int(time_input[:2]), minutes=int(time_input[3:]))
        t2 = datetime.timedelta(hours=int(time_output[:2]), minutes=int(time_output[3:]))
        delta = t2 - t1

        if delta >= datetime.timedelta(hours=1):
            outputfile.write(f'{content[0]} {content[1]}\n')
