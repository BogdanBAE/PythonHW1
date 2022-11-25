# 5'. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
import math

print('Введите координаты точки А ')
ax = int(input("х = "))
ay = int(input("y = "))
print('Введите координаты точки B ')
bx = int(input("х = "))
by = int(input("y = "))

d = float(math.sqrt(pow((bx-ax), 2) + pow((by-ay), 2)))
print(round(d, 3))
