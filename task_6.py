# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,

from itertools import count

for el in count(int(input('Введите число: '))):
    print(el)

# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle

my_list = [777, 'Привет', False, 25.25, None]
for el in cycle(my_list):
    print(el)
