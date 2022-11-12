#### TASK 01 ####
# Создайте функцию для отображения текущего времени.
# Функция не принимает параметров. Функция не используя синтаксис декораторов, произведите декорирование
# функции с помощью другой функции. Потенциальный вывод данных на экран:
# ***************************
# 23:00
# ***************************
# В этом выводе на экран две линии из звездочек – результаты декорирования.

#### TASK 02 ####
# Добавьте ещё одну функцию для декорирования вывода данных.
# Эта функция должна добавить новые элементы в форматирование вывода.

#### TASK 03 ####
# Решите задачу из первого задания с использованием синтаксиса декораторов.
import datetime
import time


def starsDecor(func):
    def wrapper():
        print("*" * 23)
        func()
        print("*" * 23)
    return wrapper


def nameFunc(func):
    def wrapper():
        print("-" * 6 + " Time Info " + "-" * 6)
        func()
    return wrapper()


def getFuncTime(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function time: {end - start}")
    return wrapper


@nameFunc
@getFuncTime
@starsDecor
def getCurrentTime():
    now = datetime.datetime.now()
    print(f"Current time: {now.hour}:{now.minute}:{now.second}")

