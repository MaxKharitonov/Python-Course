# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random 

array_len = int(input('\nВведите длину массива: ')) # Запрос длины массива.
array = [random.randint(0, 1) for i in range(array_len)] # Инициализация массива заданной длины и заполнение его
                                                         # целочисленными значениями от 0 до 1, в случайном порядке,
                                                         # где 0 - реверс, 1 - аверс монеты.
print('\nПолученный массив: {}\n'.format(array)) # Вывод полученного массива.

def min_flips(array): # Создание функции, считающей минимальное количество монет, которые нужно перевернуть.
    count = 0 # Инициализация переменной, считающей количество монет, которые перевернуты не будут.
    flips = 0 # Инициализация переменной, считающей количество монет, которые будут перевернуты.
    for i in range(len(array)): # Запуск цикла, проверяющего какой стороной лежит монета.
        if array[i] == 0: # Если монета лежит реверсом вверх,
           array[i] = 1 # то она будет перевернута.
           flips += 1 # Счетчик монет, которые были перевернуты.
        else:
            count += 1 # Счетчик монет, которые не нужно переворачивать.
    # print('Конечный массив: {}\n'.format(array)) # Вывод конечного массива.
    if count < flips: # Если монет, которые не нужно переворачивать меньше,
        return count # возвращается их количество в конечный результат.
    else:
        return flips # Если монет, которые нужно перевернуть меньше,
                     # возвращается их количество в конечный результат.
print('Минимальное количество монет, которые нужно перевернуть: {}\n'.format(min_flips(array))) 
# Вызов функции, находящей минимальное количество монет, которые нужно перевернуть и вывод результата ее работы в консоль.
print('Конец программы...\n')