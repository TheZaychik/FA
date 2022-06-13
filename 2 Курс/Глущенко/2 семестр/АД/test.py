import string

цифра = [0] * 3 * 5  # заполненная нулями матрица 3х5
цифры = цифра * 10  # резервируем память под маски 10-ти цифр
название = [""] * 10  # резервируем память под идентификаторы 10-ти цифр
допОшибок = 2
название[0] = "ноль"  # задаём перцептрону начальное знание трёх шаблонов цифр
цифра[0] = \
    [0, 1, 0,
     1, 0, 1,
     1, 0, 1,
     1, 0, 1,
     0, 1, 0]
название[1] = "единица"
цифра[1] = \
    [0, 1, 0,
     1, 1, 0,
     0, 1, 0,
     0, 1, 0,
     1, 1, 1]
название[2] = "двойка"
цифра[2] = \
    [1, 1, 1,
     1, 0, 1,
     0, 0, 1,
     0, 1, 0,
     1, 1, 1]
название[3] = "три"
цифра[3] = \
    [1, 1, 1,
     0, 0, 1,
     0, 1, 1,
     0, 0, 1,
     1, 1, 1]
название[4] = "четыре"
цифра[4] = \
    [1, 0, 1,
     1, 0, 1,
     1, 1, 1,
     0, 0, 1,
     0, 0, 1]
название[5] = "пять"
цифра[5] = \
    [1, 1, 1,
     1, 0, 0,
     1, 1, 1,
     0, 0, 1,
     1, 1, 1]
название[6] = "шесть"
цифра[6] = \
    [1, 1, 1,
     1, 0, 0,
     1, 1, 1,
     1, 0, 1,
     1, 1, 1]
название[7] = "семь"
цифра[7] = \
    [1, 1, 1,
     0, 0, 1,
     0, 1, 0,
     1, 0, 0,
     1, 0, 0]
название[8] = "восемь"
цифра[8] = \
    [1, 1, 1,
     1, 0, 1,
     1, 1, 1,
     1, 0, 1,
     1, 1, 1]
название[9] = "девять"
цифра[9] = \
    [1, 1, 1,
     1, 0, 1,
     1, 1, 1,
     0, 0, 1,
     1, 1, 1]

знает = 10  # сколько цифр теперь знает перцептрон

бесконечно = 0
while бесконечно == 0:  # бесконечный повтор программы

    # пользователь вводит образ для распознования
    print(""" 
\nВведите построчно визуальный образ цифры по три элемента в строке.
Чёрные точки обозначайте единицами, белые точки нулями.
Цифры разделяйте пробелом.
Для выхода из программы введите 5\n
    """)
    искомое = [0] * 0  # резервируем память под переменную (список из 0 элементов заполненный нулями)
    for i in range(0, 5):  # повторяем 5 раз
        приглашение = "Введите " + str(i + 1) + "-ую строку образа: "  # формируем приглашение для ввода каждой строки
        строка = list(map(int, input(приглашение).split()))  # пользователь вводит данные в переменную СТРОКА
        if строка[0] == 5:
            exit()
        искомое = искомое + строка  # добавляем строку к переменной ИСКОМОЕ
    # теперь ИСКОМОЕ стало матрицей 3x5 пользовательский ввод завешён

    # теперь проводим поиск ИСКОМОГО среди известных программе образов
    известна = 0  # картинка нам неизвестна (пока не искали)
    for i in range(0, знает):  # перебираем все цифры, которые ЗНАЕТ программа
        несовпадение = 0  # предполагаем что ИСКОМОЕ совпадает с проверяемой ЦИФРОЙ
        for j in range(0, 14):  # для всех 15-ти элементов ЦИФРЫ
            if искомое[j] != цифра[i][j]:  # если найдены неравные элементы
                несовпадение += 1  # отмечаем НЕСОВПАДЕНИЕ
        if несовпадение <= допОшибок:  # если все 15 элементов ЦИФРЫ совпали с ИСКОМЫМ
            известна = 1  # отмечаем, что цифра нам известна и обучение не нужно
            проц = round(100 - несовпадение / (14 / 100))
            print("\nС вероятностью " + str(проц) + "% - это " + название[i])  # печатаем название цифры
            # и переходим на начало бесконечного цикла (ждём нового ввода от пользователя)
    if известна == 1: известна = int(input("Правильное предположение? (1/0) "))
    if известна == 0:  # если цифра неизвестна
        print("Эта цифра мне неизвестна.")  # печатаем сообщение
        название[знает] = input("Введите её название: ")  # сохраняем, полученное от пользователя НАЗВАНИЕ
        цифра[знает] = искомое  # копируем содержимое введённого пользователем образа в пустое место списка ЦИФРЫ
        знает = знает + 1  # увеличиваем счётчик известных цифр на 1
        print("Спасибо, теперь я её знаю.\n")  # выводим сообщение
# возвращаемся к выполнению бесконечного цикла

# Задание:
# 1. Измените программу так, чтобы она распознавала цифры, если при вводе образа допущено не более двух ошибок.
# 2. Измените программу так, чтобы она выводила степень уверенности в распознавании введённой цифры.
# 3. Измените программу так, чтобы она распознавала полутоновые образы цифр с градациями тона от 0 до 255
#