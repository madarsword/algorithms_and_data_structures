# ID 88138404


'''
A. Поиск в сломанном массиве

Формат ввода
Функция принимает массив натуральных чисел и искомое число k.
Длина массива не превосходит 10000. 
Элементы массива и число k не превосходят по значению 10000.
В примерах:
В первой строке записано число n — длина массива.
Во второй строке записано положительное число k — искомый элемент. 
Далее в строку через пробел записано n натуральных чисел – элементы массива.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля).
Если элемент не найден, функция должна вернуть − 1.
Изменять массив нельзя.
Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 1000000 раз.

Пример 1
Ввод                            Вывод
9                               6
5
19 21 100 101 1 4 5 7 12

Пример 1
Ввод                            Вывод
2                               1
1
5 1
'''


def broken_search(nums, element) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = nums[mid]
        if mid_value == element:
            return mid
        if mid_value >= nums[left]:
            if nums[left] <= element < mid_value:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_value < element <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
