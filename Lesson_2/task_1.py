# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 7
my_float = 3.5
my_str = 'I love Python'
my_bool = True
my_list = [6, 'Hello', 2.3, False]
my_tuple = ('Hi', True, 456.7, 10)
my_dict = {'city': 'Smolensk', 'country' : 'Russia'}
super_list = [my_int, my_float, my_str, my_bool, my_list, my_tuple, my_dict]
print(super_list)
for i in super_list:
    print(f'{i} is {type(i)}')