# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите целое число n: '))
total = (number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))
print("Сумма чисел n + nn + nnn - %d" % total)