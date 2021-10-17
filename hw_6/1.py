# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.color = ''
        self.running()

    def running(self):
        for el in cycle(['Красный', 'Желтый', 'Зеленый']):
            print(el)
            if el == 'Красный':
                time.sleep(7)
            elif el == 'Желтый':
                time.sleep(2)
            elif el == 'Зеленый':
                time.sleep(5)


lights = TrafficLight()