'''
Заполнение диагоналями 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matrix = [[0 for j in range(m)] for i in range(n)]

elem = 1
for j in range(n + m - 1):
    for i in range(n):
        if j - i in range(m):
            matrix[i][j-i] = elem
            elem += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
