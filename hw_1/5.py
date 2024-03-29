# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

earnings = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if earnings > costs:
    print('Фирма работает в прибыль')
    print('Рентабельность фирмы равна {:.2f}'.format(earnings / costs))
    staff_count = int(input('Введите численность фирмы: '))
    print('Прибыль фирмы на одного сотрудника равна {:.2f}'.format((earnings - costs) / staff_count))
elif earnings < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в 0')
