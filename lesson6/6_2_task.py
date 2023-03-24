# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def input_array():
    array = []
    array_len = int(input('\nВведите длину массива: '))
    for i in range(array_len):
        array.append(random.randint(0, 99))
    print(array)
    return array


def find_indexes(array, min_num, max_num):
    for i in range(len(array)):
        if array[i] <= max_num and array[i] >= min_num:
            print(f'\nИндекс элемента: {i}\nЗначение элемента{array[i]}')
    return array


find_indexes(input_array(), int(input('\nВведите минимальное значение диапазона: ')),
             int(input('\nВведите максимальное значение диапазона: ')))
