'''
Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.
'''


# объявление функции
def is_palindrome(text):
    s = text.replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('-',
                                                                                                          '').upper()
    if s == s[::-1]:
        return True
    else:
        return False


print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
