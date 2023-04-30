'''
Tail of a File
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние 1010 строк данного файла.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести последние 1010 строк этого файла.

Примечание 1. Считайте, что исполняемая программа и файл находятся в одной папке.

Примечание 2. Если количество строк в файле меньше 1010, необходимо вывести содержимое файла полностью.
'''

filename = input()
with open(filename, encoding='utf-8') as file:
    content = file.readlines()
    count = len(content)
    if count < 10:
        for s in content:
            print(s, end='')
    else:
        res = content[-10:]
        for s in res:
            print(s, end='')
