"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

import random

listSize = int(input("Количество элементов в списке: "))
list = []
counter = 0

for i in range(0, listSize):
    list.append(random.randint(1, 10))

print(f"В списке {list}")
number = int(input("Введите искомое число: "))

for i in range(0, listSize):
    if list[i] == number:
        counter += 1

print(f"Число {number} встречается {counter} раз")

