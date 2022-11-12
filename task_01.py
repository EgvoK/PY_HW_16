#### TASK 01 ####
# Создайте функцию для отображения текущего времени.
# Функция не принимает параметров. Функция не используя синтаксис декораторов, произведите декорирование
# функции с помощью другой функции. Потенциальный вывод данных на экран:
# ***************************
# 23:00
# ***************************
# В этом выводе на экран две линии из звездочек – результаты декорирования.

import datetime


def starsDecoration():
    print("*" * 22)


def getCurrentTime():
    now = datetime.datetime.now()
    starsDecoration()
    print(f"Current time: {now.hour}:{now.minute}:{now.second}")
    starsDecoration()


getCurrentTime()
