import random


def task_9_105() -> str:
    """
    1) 9.105.  Дано слово из 12-ти букв. Переставить в обратном порядке буквы, расположенные между второй и десятой
        буквами (т. е. с третьей по девятую).

    :return: (string) {2}-{1}-{3}
    """
    inWord = ''.join(chr(random.randint(65, 122)) for i in range(0, 12))

    result = f'{inWord[:2]}-{inWord[9:1:-1]}-{inWord[-2::]}'

    print(f'Строка:\t{inWord}\nНовая:\t{result}')

    return result


def task_9_90() -> str:
    """
    2) 9.90.   Дано предложение. Все буквы е в нем заменить буквой и.

    :return:
    """
    inSentence = "Дано предложение. Все буквы е в нем заменить буквой и."
    result = ""
    lengthSent = len(inSentence)
    i = 0
    while i < lengthSent:
        symbol = inSentence[i]
        if symbol == 'е':
            result += "и"
        else:
            result += symbol
        i += 1

    print(f'Исходное предложение:\n\t{inSentence}\nРезультат:\n\t{result}')

    return result


def task_9_92() -> str:
    """
    3) 9.92.   Дано предложение. Все его символы, стоящие на четных местах, заменить буквой ы.

    :return:
    """

    inSentence = "Дано предложение. Все его символы, стоящие на четных местах, заменить буквой ы."
    lenSnt = len(inSentence)
    result = ''
    i = 0
    while i < lenSnt:
        symbol = inSentence[i]
        if i % 2 == 0: symbol = "ы"
        result += symbol

        i += 1

    print(f'Вход:\n\t{inSentence}\nВыход:\n\t{result}')

    return result


def task_9_38_a():
    """
    4) 9.38.   (при помощи срезов) Дано слово из 12 букв. Поменять местами его трети следующим образом:
            а) первую треть слова разместить на месте третьей, вторую треть — на месте первой,
                третью треть — на месте второй;
    :return: (string) {2}-{1}-{3}
    """
    inWord = ''.join(chr(random.randint(65, 122)) for i in range(0, 12))

    result = f'{inWord[4:8]}-{inWord[:4]}-{inWord[-4::]}'

    print(f'Строка:\t{inWord}\nНовая:\t{result}')

    return result


def task_9_153() -> int:
    """
    5) 9.153.  Дан текст. Найти наибольшее количество идущих подряд одинаковых символов (символ, который идёт подряд -
            вводится с клавиатуры).

    :return:
    """
    inText = 'Trtrtrtr rrrr yuy reeeeeee ieeey oereeooo eeeeee'
    symbol = 'e'

    maxSmb = ''
    maxCount = 0
    lengthText = len(inText)
    i = 0
    count = 0
    while i < lengthText:
        currentChar = inText[i]
        if currentChar == symbol and currentChar == inText[i - 1]:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
        i += 1
    else:
        if count > maxCount:
            maxCount = count
        if maxCount != 0:
            maxCount += 1

    print(f'Символ {symbol} в предложении:\n\t{inText}\n, - встречается подряд максимум {maxCount} раз.')

    return maxCount
