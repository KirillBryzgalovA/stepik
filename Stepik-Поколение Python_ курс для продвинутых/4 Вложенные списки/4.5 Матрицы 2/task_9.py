'''
Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^2
так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
Формат входных данных На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
'''


# сумма по главной диагонали
def sled_one(matrix, n):
    summa = 0
    for i in range(n):
        summa += int(matrix[i][i])
    return summa


# сумма по  вторичной диагонали
def sled_two(matrix, n):
    summa = 0
    for i in range(n):
        summa += int(matrix[i][n - i - 1])
    return summa


n = int(input())
seq = [i for i in range(1, n ** 2 + 1)]
#flag = True

matrix = []
temp_list = []  # врем. список для хранения всех чисел матрицы
for i in range(n):
    temp = [int(num) for num in input().split()]
    temp_list.extend(temp)
    matrix.append(temp)

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

a = sled_one(matrix, n)
b = sled_two(matrix, n)
c = sum(result) / len(result)
d = sum(matrix[0])

if a != b or c != d:
    print("NO")
else:
    print("YES")
