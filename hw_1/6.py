# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = 0
b = 0

while a >= b:
    a = int(input('Введите текущий результат по бегу в киллометрах: '))
    b = int(input('Введите желаемый результат по бегу в киллометрах: '))
    if a > b:
        print('Желаемый результат должен быть больше текущего')

result = a
i = 0
while result < b:
    result = result + result / 10
    i = i + 1
    print(f'{i}-й день: {round(result, 2)}')
print(f'Ответ: на {i}-й день спортсмен достиг результата - не менее {b} км.')