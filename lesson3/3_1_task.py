# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

def array_input (array_length): # Функция для заполнения массива, вводом пользователя. 
    # Принимает на вход длину массива, введенную пользователем.
    array = [] # Объявление массива.
    el_number = 1 # Счетчик элементов массива.
    for i in range(array_length): # Цикл запрашивающий ввод элементов массива.
        array_el = int(input('\nВведите {}-й элемент массива: '.format(el_number))) # Ввод элемента от пользователя.
        array.append(array_el) # Добавление, введенного элемента в массив.
        print('Текущий массив: ',array) # Вывод массива, после каждой итерации.
        el_number += 1
    return array 

def x_number_count (array, X): # Функция, считающая сколько раз встретилось число Х. 
    # Принимает на вход массив чисел и число Х.
    count = 0 
    for i in range(len(array)): # Цикл, проходящий по массиву и считающий сколько раз встреилось число Х.
        if(X == array[i]): # Проверка текущего элемента массив на равенство числу Х.
            count += 1
    if(count > 0): # Проверка на наличие числа Х в массиве.       
        print('\nВведенное число: {} встречается в массиве {} раз(а).'.format(X, count)) # Вывод результата работы программы.
    else:
        print('\nВведенного числа в массиве не найдено.') 

x_number_count(array_input(int(input('\nВведите длину массива: '))), int(input('\nВведите число, повторение которого, необходимо посчитать: ')))
    # N = int(input('\nВведите длину массива: '))
    # array = array_input(N)
    # X = int(input('\nВведите число, повторение которого, необходимо посчитать: '))
    # x_number_count(array, X)