# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

def menu (button): # Функция меню программы.
    select = None # Переменная, отвечающая за хранение выбора пользователя.
    while(True): # Запуск бесконечного цикла.
        if(button == 1): # Если выбрана первая команда.
            print('\nВыбран английский язык.') # Ответ пользователю на введенную команду.
            select = 'ENG' # Присваивание переменной выбора пользователя.
            return select # Возврат команды, выбранной пользователем, для дальнейшего использования.
        elif(button == 2): # Если выпбрана вторая команда.
            print('\nВыбран русский язык.') # Ответ пользоватею на введенную команду.
            select = 'RUS' # Присваивание пепеменной выбора пользователя.
            return select # Возврат команды, выбранной пользователем, для дальнейшего использования.
        elif(button == 0): # Если выбрана третья команда.
            print('\nВыход...') # Ответ пользователю на введенную команду.
            break # Прерырвание бесконечного цикла, завершение программы.
        else: # Если введена неизвестная команда.
            print('\nОшибка! Введена некорректная команда!') # Ответ пользователю на введенную команду.
            break # Прерывание бесконечного цикла, завершение программы, в связи с ошибкой.


def rules (letters): # Функция, выводящая необходимую информацию для пользователя.
    if(letters == 'ENG'): 
        print('\nТаблица очков:')
        print('A; E; I; O; U; L; N; S; T; R - 1 очко;')
        print('D; G - 2 очка;')
        print('B; C; M; P - 3 очка;')
        print('F; H; V; W; Y - 4 очка;')
        print('K - 5 очков;')
        print('J; X - 8 очков;')
        print('Q; Z - 10 очков.\n')
    else: 
        print('\nТаблица очков:')
        print('А; В; Е; И; Н; О; Р; С; Т - 1 очко;')
        print('Д; К; Л; М; П; У - 2 очка;')
        print('Б; Г; Ё; Ь; Я - 3 очка;')
        print('Й; Ы - 4 очка;')
        print('Ж; З; Х; Ц; Ч - 5 очков;')
        print('Ш; Э; Ю; - 8 очков;')
        print('Ф; Щ; Ъ - 10 очков;\n')


def game (LIST): # Основная функция программы.
    score = 0 # Переменная, хранящая результат.
    if(LIST == 'ENG'): # Если пользователь введ первую команду выполнится этот блок кода.
        rules('ENG') # Вывод описания.
        LIST = ENG # Присваивание списка.
        lang = 'английском' # Необходимые замены в коде, чтобы избежать его дублирования.
        alphabeth_check = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        error_lang = 'английских'
    elif(LIST == 'RUS'): # Если пользователь ввел вторую команду выполнится это блок кода.
        rules('RUS') # Вывод описания.
        LIST = RUS # Присваивание списка.
        lang = 'русском' # Необходимые замены в коде, чтобы избежать его дублирования.
        alphabeth_check = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
        error_lang = 'русских'
    else: # Если пользователь ввел третью команду или ошибся при вводе команды, выполнится этот блок кода.
        return # Завершение программы, с случае с третьей команды или ощибки ввода.
    word = str(input('Введите слово на {} языке: \n'.format(lang)).upper()) # Запрос ввода слова от пользователя и приведение его в верхний регистр.
    if(word.isalpha() and all(letter in alphabeth_check for letter in word)): # Проверка соответствия выбранного языка с введенным.
        score = sum(LIST.get(letter, 0) for letter in word) # Подсчет результата, получение значений ключей списка имеющихся во введенном слове.
        print('\nВведенное слово набрало: {} очков.'.format(score)) # Вывод результата.
    else: # Если введенные буквы не соответствуют выбранному языку, вызывавется сообщение об ошибке.
        print('\nОшибка! Слово должно состоять из {} букв!'.format(error_lang)) # Вывод ошибки.

ENG = {'A':1,'E':1,'I':1,'O':1,'U':1,'L':1,'N':1,'S':1,'T':1, 
       'R':1,'D':2,'G':2,'B':3,'C':3,'M':3,'P':3,'F':4,'H':4,
       'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10} # Список, хранящий ключи и их значения, для английского языка.
RUS = {'А':1,'В':1,'Е':1,'И':1,'Н':1,'О':1,'Р':1,'С':1,'Т':1,
       'Д':2,'К':2,'Л':2,'М':2,'П':2,'У':2,'Б':3,'Г':3,'Ё':3,
       'Ь':3,'Я':3,'Й':4,'Ы':4,'Ж':5,'З':5,'Х':5,'Ц':5,'Ч':5,
       'Ш':8,'Э':8,'Ю':8,'Ф':10,'Щ':10,'Ъ':10} # Список, хранящий ключи и их значения, для русского языка.

game(menu(int(input('\nВыберите язык:\n\n1 - ENG\n2 - RUS\n0 - EXIT\n')))) # Запуск программы.