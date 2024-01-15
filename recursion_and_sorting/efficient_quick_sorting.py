# ID 88174258


'''
B. Эффективная быстрая сортировка

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
- уникальным логином (строкой из маленьких латинских букв длиной не более 20);
- числом решённых задач Pi;
- штрафом Fi.
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 10**9.

Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.

Пример 1
Ввод                            Вывод
5                               gena
alla 4 100                      timofey
gena 6 1000                     alla
gosha 2 90                      gosha
rita 2 90                       rita
timofey 4 80

Пример 1
Ввод                            Вывод
5                               alla
alla 0 0                        gena
gena 0 0                        gosha
gosha 0 0                       rita
rita 0 0                        timofey
timofey 0 0
'''


def quicksort(arr, compare_func=lambda x, y: x < y):
    def partition(start, end):
        pivot = arr[end]
        smaller_index = start - 1
        for current_index in range(start, end):
            if compare_func(arr[current_index], pivot):
                smaller_index += 1
                (
                    arr[smaller_index], arr[current_index]
                ) = (
                    arr[current_index], arr[smaller_index]
                )
        arr[smaller_index + 1], arr[end] = arr[end], arr[smaller_index + 1]
        return smaller_index + 1

    def quick_sort(start, end):
        if start < end:
            pivot_index = partition(start, end)
            quick_sort(start, pivot_index - 1)
            quick_sort(pivot_index + 1, end)
    quick_sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    num_participants = int(input())
    input_data = [input().split() for _ in range(num_participants)]
    participants = [(participant_id, int(completed_tasks), int(fine))
                    for participant_id, completed_tasks, fine in input_data]
    participants = quicksort(
        participants, compare_func=lambda x, y: (x[1] > y[1])
        or (x[1] == y[1] and x[2] < y[2])
        or (x[1] == y[1] and x[2] == y[2] and x[0] < y[0])
    )
    print(*[participant[0] for participant in participants], sep='\n')
