# ID 87414710


'''
B. Ловкость рук

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы значения для кнопок –— по 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— количество баллов, которое игроки наберут в раунде.

Пример 1
Ввод                Вывод
3                   2
1231
2..2
2..2
2..2

Пример 2
Ввод                Вывод
4                   1
1111
9999
1111
9911

Пример 3
Ввод                Вывод
4                   0
1111
1111
1111
1111
'''


def sleight_of_hand(field, key):
    keys_press = key * 2
    return sum(
        0 < field.count(digit) <= keys_press for digit in '123456789'
    )


if __name__ == '__main__':
    key = int(input())
    field = [char for _ in range(4) for char in input()]
    print(sleight_of_hand(field, key))
