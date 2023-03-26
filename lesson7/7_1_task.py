# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
#           *Пример:*
#           **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#           **Вывод:** Парам пам-пам
 
# def count_vowels(phrase): # Функция для подсчета гласных в слове.
#     count = lambda word: len(list(filter(lambda letter: letter in 'eyuioa', word))) #

##### сохранить в функцию count() из массива слов (lambda word), полученную длину(len()) массива (количество) гласных букв(list()), 
##### найденых в каждом массиве букв(lambda letter), преобразованном из слов(word)
    ### count - подсчет гласных букв.
    ### lambda - получение массива слов из фразы.
    ### word - элемент(слово) массива слов
    ### len - определение длины массива гласных.
    ### list - массив гласных букв, найденый функцией filter(),
    ### filter - подсчет гласных букв, в каждом массиве букв,
    ### lambda - получение массива букв из слова.
    ### letter - элемент(буква) массива букв.
    ### in 'eyuioa' - если буква является гласной.

#     return sum(count(word) for word in phrase.split('-')) # 
##### сохранить в функцию sum() количество всех гласных(count()), найденных в каждом элементе(слове(word)) массива слов. 
    ### count() - подсчет гласных букв.
    ### word - элемент(слово) массива слов.
    ### phrase.split('-') - получение массива слов из фразы.
    ### count(word) for word in phrase.split('-') - сохранение количества, найденых в каждом элементе(слове) массива слов, глассных.
    ### sum - подсчет общего количества гласных букв из массива слов.








# 1. Использование цикла `for` и условного оператора `if`:

# def count_vowels(word):
#     count = 0
#     for letter in word:
#         if letter in 'aeiouy':
#             count += 1
#     return count

# def count_vowels_in_phrase(phrase):
#     words = phrase.split('-')
#     counts = []
#     for word in words:
#         counts.append(count_vowels(word))
#     return sum(counts)

# poem = input()
# phrases = poem.split()
# vowels_counts = [count_vowels_in_phrase(phrase) for phrase in phrases]

# if len(set(vowels_counts)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# 2. Использование метода `count()`:

# def count_vowels_in_word(word):
#     vowels = 'aeiouy'
#     return sum(word.count(letter) for letter in vowels)

# def count_vowels_in_phrase(phrase):
#     words = phrase.split('-')
#     return sum(count_vowels_in_word(word) for word in words)

# poem = input()
# phrases = poem.split