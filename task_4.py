# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_num = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_num:
        max_num = number % 10
    number = number // 10
print(f'Самая большая цифра в числе - {max_num}')