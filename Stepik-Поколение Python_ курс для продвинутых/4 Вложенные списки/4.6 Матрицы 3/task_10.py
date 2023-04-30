'''
Заполнение спиралью 😈😈
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matrix = [[0 for j in range(m)] for i in range(n)]

direction = ['right', 'bottom', 'left', 'top']

elem = 1

current_dir = direction[0]
i = 0
j = 0
while elem <= n * m:
    matrix[i][j] = elem
    elem += 1
    if current_dir == 'right':
        if j + 1 == m or matrix[i][j + 1] != 0:
            current_dir = direction[1]  # меняем направление на bottom
            i += 1
        else:
            j += 1
    elif current_dir == 'bottom':
        if i + 1 == n or matrix[i + 1][j] != 0:
            current_dir = direction[2]  # меняем направление на left
            j -= 1
        else:
            i += 1
    elif current_dir == 'left':
        if j == 0 or matrix[i][j - 1] != 0:
            current_dir = direction[3]  # меняем направление на top
            i -= 1
        else:
            j -= 1
    elif current_dir == 'top':
        if matrix[i - 1][j] != 0:
            current_dir = direction[0]  # меняем направление на right
            j += 1
        else:
            i -= 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
