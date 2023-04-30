'''
Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matA = []
for _ in range(n):
    temp = [int(num) for num in input().split()]
    matA.append(temp)

input()

arr = [int(i) for i in input().split()]
m = arr[0]
k = arr[1]

matB = []
for _ in range(m):
    temp = [int(num) for num in input().split()]
    matB.append(temp)

for i in range(n):
    for j in range(k):
        s = 0
        for r in range(m):
            s += matA[i][r] * matB[r][j]
        print(s, end=' ')
    print()
