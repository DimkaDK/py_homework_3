"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
"""

import random

listSize = int(input("Количество элементов в списке: "))
list = []

for i in range(0, listSize):
    list.append(random.randint(1, 10))

print(f"В списке {list}")
number = int(input("Введите искомое число: "))
min = 0

for i in range(1, listSize):
    if (list[i - 1] - number) > (list[i] - number):
        min = i

print(f"К числу {number} наиболее близко стоит число {list[min]}")
