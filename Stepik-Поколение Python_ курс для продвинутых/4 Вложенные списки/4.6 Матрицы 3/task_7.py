'''
Заполнение 5 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matrix = [[0 for j in range(m)] for i in range(n)]

arr_fill = [i for i in range(1, m + 1)]

for i in range(n):
    matrix[i] = list(arr_fill)
    elem = arr_fill.pop(0)
    arr_fill.append(elem)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
