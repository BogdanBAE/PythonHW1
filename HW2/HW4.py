# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2
import os
os.chdir(r'D:\Geek Brains\Python\1lection\1seminar\HW2\file.txt')
with open('file.txt', 'r') as f:
    position = f.read().split('\n')
position = list(map(int, position))

n = int(input("Введите число: "))
list = [i for i in range(-n, n=1)]
result = 1
for i in position:
    result *= list[i]
print(position)
print(list)
print(result)
