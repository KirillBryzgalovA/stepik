'''
 Латинский квадрат 🌶️
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
'''

n = int(input())

matrix = []
temp_list = []  # врем. список для хранения всех чисел матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]
    temp_list.extend(temp)
    matrix.append(temp)

seq = [i for i in range(1, n + 1)]

# Проверка условия - каждая строка и каждый столбец которой содержат все числа от 11 до nn
for elem in seq:
    if elem not in list(set(temp_list)):
        print("NO")
        exit(0)

trans_matrix = [[matrix[i][j] for i in range(n)] for j in range(n)]

result = []
# для анализа используем список
# получаем суммы строк и столбцов
for i in range(n):
    result.append(sum(matrix[i]))
    result.append(sum(trans_matrix[i]))

if len(set(result)) > 1:
    print("NO")
else:
    print("YES")
