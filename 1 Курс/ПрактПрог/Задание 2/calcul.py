import math

operation_list = [
    'плюс',
    'минус',
    'умножить',
    'поделить',
    'размещение',
    'сочетание',
    'перестановка',
]
numbers = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнаддцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
}
number1, number2 = 0, 0


def get_numbers(pos, str_input):
    global number1, number2
    for num in numbers:
        for j in range(len(str_input)):
            if num == str_input[j]:
                if j < pos:
                    number1 += numbers[num]
                elif j > pos:
                    number2 += numbers[num]


def calc():
    global number1, number2
    pos = 0
    operation = 0
    print('Введите строку:')
    str_input = input().split(' ')
    for i in range(len(operation_list)):
        for j in range(len(str_input)):
            if operation_list[i] == str_input[j]:
                pos = j
                operation = i
    if operation < 4:
        get_numbers(pos, str_input)

    else:
        if operation < 6:
            for j in range(len(str_input)):
                if 'по' == str_input[j]:
                    pos = j
            get_numbers(pos, str_input)
        else:
            for num in numbers:
                for j in range(len(str_input)):
                    if num == str_input[j]:
                        number1 += numbers[num]

    if operation == 0:
        print('Ответ:', number1 + number2)
    elif operation == 1:
        print('Ответ:', number1 - number2)
    elif operation == 2:
        print('Ответ:', number1 * number2)
    elif operation == 3:
        print('Ответ:', number1 / number2)
    elif operation == 4:
        print('Ответ:', math.factorial(number1) / math.factorial(number1 - number2))
    elif operation == 5:
        print('Ответ:', math.factorial(number1) / (math.factorial(number2) * math.factorial(number1 - number2)))
    elif operation == 6:
        print('Ответ:', math.factorial(number1))


if __name__ == '__main__':
    calc()
