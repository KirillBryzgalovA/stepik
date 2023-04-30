'''
Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
'''

import string
import random

digits = string.digits.replace('0', '').replace('1', '')
lowercases = string.ascii_lowercase.replace('l', '').replace('o', '')
uppercases = string.ascii_uppercase.replace('I', '').replace('O', '')

n, m = int(input()), int(input())


def generate_password(length):
    print(random.choice(uppercases), end='')
    print(random.choice(digits), end='')
    print(random.choice(lowercases), end='')
    for _ in range(length - 3):
        sym = random.choice(uppercases + lowercases + digits)
        print(sym, end='')


def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)
        print()


generate_passwords(n, m)
