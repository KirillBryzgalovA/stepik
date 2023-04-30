'''
Конкатенация файлов 🌶️
На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число nn и nn строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
'''

n = int(input())

arr_files = [input().strip() for _ in range(n)]
with open('output.txt', 'a', encoding='utf-8') as outputfile:
    for filename in arr_files:
        with open(filename, encoding='utf-8') as inputfile:
            content = inputfile.readlines()
        outputfile.writelines(content)

