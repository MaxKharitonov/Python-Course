# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 
# *Пример:*
# 
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input('Введите общее количество журавликов, сделанное ребятами: ')) # Запрос ввода количества журавликов.
print(f'\nОбщее количество журавликов, сделанное ребятами: {s}\n')
if (s % 2 != 0 and s % 6 != 0):
    print('Ошибка! Введенное число нечетное или не кратно 6! Ребята не могут сделать только часть журавлика!\nКонец программы...\n')
else:    
    katya = s // 2 # Получение количества журваликов, сделанных Катей. 
    petya_and_sereja = katya // 2 # Получение количества журавликов, сделанных Петей и Сережей.
    print('Катя сделала {} журавлика(ов), Петя и Сережа сделали по {} журавлика(ов)\n'.format(katya, petya_and_sereja)) # Вывод результата.
    print('Конец программы...')