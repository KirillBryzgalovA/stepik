'''
Значение многочлена 🌶️
На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число xx на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении xx.

Формат входных данных
На вход программе на первой строке подаются коэффициенты многочлена (целые числа), разделенные символом пробела и целое число xx на второй строке.
'''
from functools import reduce

coefficients = [int(i) for i in input().split()]
x = int(input())


def evaluate(coefficients, x):
    arr = list(
        map(lambda c, z, n: c * z ** n, coefficients, [x] * len(coefficients), range(len(coefficients) - 1, -1, -1)))
    reduce_result = reduce(lambda x, y: x + y, arr, 0)
    print(reduce_result)


evaluate(coefficients, x)
