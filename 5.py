# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [7, 5, 3, 3, 2]

while True:
    dig = int(input('Введите число: '))

    try:
        my_list.insert(my_list.index(dig) + my_list.count(dig), dig)
    except ValueError:
        for elem_list in my_list:
            if elem_list < dig:
                my_list.insert(my_list.index(elem_list), dig)
                break
    print(my_list)

# P.S. По заданию вроде не надо было делать его возрастающим, но я сделал))
