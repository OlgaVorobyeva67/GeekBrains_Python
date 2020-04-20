# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input('Введите номер месяца: '))
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if number == 1 or number == 12 or number == 2:
    print(seasons_dict.get(1), seasons_list[0])
elif number == 3 or number == 4 or number == 5:
    print(seasons_dict.get(2), seasons_list[1])
elif number == 6 or number == 7 or number == 8:
    print(seasons_dict.get(3), seasons_list[2])
elif number == 9 or number == 10 or number == 11:
    print(seasons_dict.get(4), seasons_list[3])
else:
    print("Такого месяца не существует")
