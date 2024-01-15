# ID 87988735


'''
B. Калькулятор

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.

Пример 1
Ввод                Вывод
2 1 + 3 *           9

Пример 1
Ввод                Вывод
7 2 + 4 * 2 +       38
'''


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
    '*': lambda x, y: x * y
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        raise IndexError('Стек пуст')


def calculator(polish_notation):
    stack = Stack()
    for element in polish_notation:
        if element in OPERATORS:
            number_1, number_2 = stack.pop(), stack.pop()
            stack.push(OPERATORS[element](number_2, number_1))
        else:
            stack.push(int(element))
    return stack.pop()


if __name__ == '__main__':
    polish_notation = input().split()
    print(calculator(polish_notation))
