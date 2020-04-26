# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    payment = time * salary + bonus
    print(f"Заработная плата сотрудника составит {payment} рупий")
except ValueError:
    print('Вы ввели не число')
