'''
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
'''


# объявление функции
def is_correct_bracket(text):
    count = 0

    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        if count < 0:
            break

    if count == 0:
        return True
    return False
    # a = text.count('(')
    # b = text.count(')')
    # if a == b and text.startswith('(') and text.endswith(')'):
    #     return True
    # else:
    #     return False


print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
print(is_correct_bracket('())(()'))
print(is_correct_bracket('())((((())))'))
