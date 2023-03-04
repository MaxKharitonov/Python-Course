# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 
# *Пример:*
# 
# 385916 -> yes
# 123456 -> no

ticket_number = int(input('Введите номер билета: ')) # Запрос ввода номера билета.
print('\nНомер билета: {}\n'.format(ticket_number))
if (ticket_number > 999999): # Проверки на корректность введенного числа.
    print('Ошибка! Номер билета должен быть шестизначным!\n') # Вывод ошибки, если число больше шестизначного.
    print('Введенное число больше!\nЗапустите программу заново и введите корректное число.\nКонец программы...')
elif (ticket_number < 100000):
    print('Ошибка! Номер билета должен быть шестизначным!\n') # Вывод ошибки, если число меньше шестизначного.
    print('Введенное число меньше!\nЗапустите программу заново и введите корректное число.\nКонец программы...')
else:
    first_digit = ticket_number // 100000 # Получение первой цифры номера билета.
    print('Первая цифра билета: {}'.format(first_digit))
    second_digit = (ticket_number // 10000) % 10 # Получение второй цифры номера билета.
    print('Вторая цифра билета: {}'.format(second_digit))
    third_digit = (ticket_number // 1000) % 10 # Получение третьей цифры номера билета.
    print('Третья цифра билета: {}'.format(third_digit))
    fourth_digit = (ticket_number // 100) % 10 # Получение четвертой цифры номера билета.
    print('Четвертая цифра билета: {}'.format(fourth_digit))
    fifth_digit = (ticket_number // 10) % 10 # Получение пятой цифры номера билета.
    print('Пятая цифра билета: {}'.format(fifth_digit))
    sixth_digit = ticket_number % 10 # Получение шестой цифры номера билета.
    print('Шестая цифра билета: {}\n'.format(sixth_digit))
    first_three_digits_sum = first_digit + second_digit + third_digit # Нахождение суммы первых трех цифр номера билета.
    print('Сумма первых трех цифр номера билета: {}'.format(first_three_digits_sum))
    last_three_digits_sum = fourth_digit + fifth_digit + sixth_digit # Нахождение суммы последних трех цифр номера билета.
    print('Сумма последних трех цифр номера билета: {}\n'.format(last_three_digits_sum))
    if (first_three_digits_sum == last_three_digits_sum): # Проверка на равенство сумм первых и последних цифр номера билета.
        print('Введенный номер билета {} является счастливым!\nКонец программы...'.format(ticket_number)) # Вывод результата
    else:
        print('Введенный номер билета {} не является счастливым!\nКонец программы...'.format(ticket_number))