# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

import re

my_list = ['Информатика: 100(л) 50(пр) 20(лаб)\nФизика: 30(л) - 10(лаб)\nФизкультура: - 30(пр) -']
with open('text_6.txt', 'w+') as f:
    f.write(my_list[0])

with open('text_6.txt', 'r') as f:
    print(f.read())

with open('text_6.txt', 'r', encoding='utf-8') as f:
    subj = {}
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = sum(int(i) for i in re.findall(r'\d+', lecture + practice + lab))
    print(subj)