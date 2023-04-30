'''
Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в mm-ую степень.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число mm.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
import copy

matA = []
n = int(input())

for _ in range(n):
    temp = [int(num) for num in input().split()]
    matA.append(temp)

num = int(input())
cur_matrix = copy.deepcopy(matA)

for _ in range(num - 1):
    temp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                temp[i][j] += cur_matrix[i][r] * matA[r][j]
    cur_matrix = copy.deepcopy(temp)

for i in range(n):
    for j in range(n):
        print(cur_matrix[i][j], end=' ')
    print()
