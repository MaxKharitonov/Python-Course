# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
#           *Пример:*
#           **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#           **Вывод:** Парам пам-пам

### ************************************************************************************************************************************ ###
###                                             Сокращенный вариант решения задачи                                                       ###
### ************************************************************************************************************************************ ###

def count_vowels(phrase): # Функция, считающая количество гласных.
    count = lambda word: len(list(filter(lambda letter: letter in 'eyuioaуеыаоэяию', word)))
    return sum(count(word) for word in phrase.split('-'))

# def sum_vow (arr):
#     vow_sum = 0
#     for i in range(len(arr)):
#         vow_sum += arr[i]
#         if vow_sum != 0:
#             count_vowels(phrases)
#         else:
#             print(f'\nНет гласных!')

text = input(f'\nВведите текст стихотворения: ') # Ввод текста стихотворения.
phrases = text.split() # Разбитие исходного текста на фразы.
vowels_counts = [count_vowels(phrase) for phrase in phrases] # Получение количества гласных в каждом слове, каждой фразы.
vow_sum = 0
# rhyme = vowels_counts[0]
for i in range(len(vowels_counts)):
    vow_sum += vowels_counts[i]
    print(f'\nVowCount: {vowels_counts[i]}, index: {i}, VowSum: {vow_sum}')
if vow_sum != 0:
    rhyme = vowels_counts[0]
    if vowels_counts[i] == rhyme:
        print(f'\nПарам пам-пам!')
    else:
        print(f'\nПам парам!')
else:
    print(f'\nГласных нет!') 
    
### ************************************************************************************************************************************ ###
###                                             Развернутый вариант решения задачи:                                                      ###
### ************************************************************************************************************************************ ###

# def vowel_count(phrases): # Функция считающая гласные.
#     vow_arr = [] # Объявление массива, хранящего гласные буквы всех слов.
#     print(f'\nТекущая фраза стихотворения: "{phrases}"') # Информационный вывод.
#     for word in range(len(phrases)): # Цикл, разбивающий фразы на буквы.
#         letters = list(phrases[word]) # Получение массива букв из слов.
#         for letter in range(len(letters)): # Цикл, проверяющий, является ли буква гласной.
#             if letters[letter] == '-': # Пропуск дефиса во фразе.
#                 letter += 1 # Переход к следующему элементу массива(букве), если встретился дефис.
#             # Здесь можно добавить проверку на символы отличные от букв. Но мне пока лень.
#             else: # Продолжаение програмы, если дефис не встретился.
#             # Проверка, является ли буква гласной. Можно сделать проще, но хочу чтобы было все разжевано до нельзя. Для себя.
#                 if letters[letter] == 'e' or letters[letter] == 'y' or letters[letter] == 'u' or letters[letter] == 'i' or letters[letter] == 'o' or letters[letter] == 'a' or letters[letter] == 'у' or letters[letter] == 'е' or letters[letter] == 'ы' or letters[letter] == 'а' or letters[letter] == 'о' or letters[letter] == 'э' or letters[letter] == 'я' or letters[letter] == 'и' or letters[letter] == 'ю': 
#                     vowel = letters[letter] # Инициализация переменной, хранящей гласную.
#                     vow_arr.append(vowel) # Добавление гласной в массив гласных.
#     return len(vow_arr) # Получение длины массива гласных. Завершение работы функции.

# def is_rythmic (array): # Функция, проверяющая ритм стихотворения. Сравнение количества гласных в каждой фразе.
#     rythm = array[0]
#     for quan in range(len(array)): # Цикл сравнивающий количество гласных во фразах.
#         if array[quan] != rythm: # Проверка равенства гласных между фразами.
#             result = '\nПам парам!\n' # Если количество гласных разнное, вывод сообщения, о том, что у стихотворения нет ритма.
#             break # Завершение работы цикла и программы, если во фразах, разное количество гласных.
#         else: # Продолжение работы цикла, если количество гласных во фразах равно.
#             result = '\nПарам пам-пам!\n' # Вывод сообщения, о том, что у стихотворения есть ритм.
#     return result # Завершение работы функции и вывод результата.

# text = input('\nВведите текст стихотворения: \n') # Запрос ввода текста стихотворения.
# phrases = text.split() # Разделение исходной строки, на фразы.
# number_of_vowels = [] # Объявление массива, хранящего количество гласных в каждой фразе.
# phrase_number = 1 # Счетчик фраз, для информационного сообщения.

# for phrase in range(len(phrases)): # Цикл, передающий массив фраз, в функцию подсчета гласных.
#     vowels = vowel_count(phrases[phrase]) # Инициализация переменной, хранящей количество гласных и получение его из функции подсчета.
#     print(f'Количество найденых гласных в {phrase_number}-й фразе: {vowels}') # Информационное сообщение.
#     phrase_number += 1 # Сдвиг счетчика фраз информационного сообщения.
#     number_of_vowels.append(vowels) # Добавление, найденого количества гласных каждой фразы, в массив, хранящий количество гласных. 
#     vow_sum = 0 # Инициализация переменной, хранящей сумму элементов массива, содержащего количество гласных во фразах.
#     for i in range(len(number_of_vowels)): # Цикл, перебирающий элементы массива.
#         vow_sum += number_of_vowels[i] # Суммирование элементов массива.
# if vow_sum != 0: # Если сумма элементов не равна 0, программа продолжает работу.
#     print(is_rythmic(number_of_vowels)) # Вывод результата работы программы.
# else: # Если сумма равна 0, значит гласных в веденном тексте нет.
#     print(f'\nОтсутствуют гласные!\n') # Вывод сообщения об отсутствии гласных и завершение программы.
        

### ************************************************************************************************************************************ ###
###                                             **********************************************  
### ************************************************************************************************************************************ ###