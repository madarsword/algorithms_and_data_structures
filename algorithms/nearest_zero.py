# ID 87357074


'''
A. Ближайший ноль.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 10**6).
В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 10**9.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

Пример 1
Ввод                Вывод
5                   0 1 2 1 0
0 1 4 9 0

Пример 2
Ввод                Вывод
6                   0 1 2 3 4 5
0 7 9 4 8 20
'''


def nearest_zero(street, n):
    distances = [0] * num_houses
    nearest_zero = num_houses + 1

    # left to right
    for i, house in enumerate(street):
        if house == 0:
            nearest_zero = 0
        else:
            nearest_zero += 1
        distances[i] = nearest_zero
    nearest_zero = num_houses + 1

    # right to left
    for i in range(num_houses - 1, -1, -1):
        if street[i] == 0:
            nearest_zero = 0
        else:
            nearest_zero += 1
        distances[i] = min(distances[i], nearest_zero)
    return distances


if __name__ == '__main__':
    num_houses = int(input())
    street = [int(house) for house in input().split()]
    result = nearest_zero(street, num_houses)
    print(*result, sep=' ', end='')
