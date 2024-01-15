# ID 87989203


'''
A. Дек

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека.
Он не превосходит 50000.
В следующих n строках записана одна из команд:
- push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
- push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
- pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
- pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод                Вывод
4                   861
4                   -819
push_front 861
push_front -819
pop_back
pop_back

Пример 2
Ввод                Вывод
7                   -855
10                  0
push_front -855     844
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823

Пример 3
Ввод                Вывод
6                   20
6                   102
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
'''


class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elem = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value):
        if self.is_full():
            raise IndexError('Дек заполнен')
        self.elem[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise IndexError('Дек заполнен')
        self.head = (self.head - 1) % self.max_size
        self.elem[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Дек пуст')
        back = self.elem[self.tail - 1]
        self.elem[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return back

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Дек пуст')
        front = self.elem[self.head]
        self.elem[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return front


if __name__ == '__main__':
    command_length = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(command_length):
        command, *data = input().split()
        try:
            output = getattr(deque, command)(*data)
        except IndexError:
            output = 'error'
        if output is not None:
            print(output)
