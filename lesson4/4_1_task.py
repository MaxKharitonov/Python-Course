# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def array_input(length):  # Функция заполнения массива
    array = []
    el_number = 1
    for i in range(length):
        input_array = int(input(f'\nВведите {el_number}-й элемент массива: '))
        array.append(input_array)
        el_number += 1
        print(array)
    return array


def equal_elements(array1, array2):
    array = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                number = array1[i]
                array.append(number)
                print(array)


arr1 = array_input(int(input('\nВведите длину первого массива:')))
arr2 = array_input(int(input('\nВведите длину второго массива:')))
equal_elements(arr1, arr2)
