# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

my_dict = {}
with open("7", "r", encoding='utf-8') as file:
    lines = file.readlines()
    all_profit = 0
    for line in lines:
        my_line = line.split()
        my_dict[str(my_line[0])] = int(my_line[2]) - int(my_line[3])
        all_profit += my_dict[my_line[0]]
    result = [my_dict, {"average_profit": all_profit / len(my_dict)}]

with open('7.json', 'w') as f_json:
    json.dump(result, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))
