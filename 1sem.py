# # Вывести квадрат числа

# a = int(input())

# print(pow(a, 4))

# Напишите программу которая принимает на вход число и проверяет, является ли оно квадратом друго

# print("Введите первое число ")
# a = int(input())
# print("Введите второе число ")
# b = int(input())

# if a**2 == b or b**2 == a:
#     print('является')
# else:
#     print('Не является')

# Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них.

# a = input().split()
# print(a)
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i]) > max:
#         max = int(a[i])
# print(max)

# a = list(map(int, input().split))
# print(max(a))

# print("Введите число ")
# a = float(input())

# b = int(a*10 % 10)
# print(b)

2

if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and not (a % 30 == 0):
    print('Подходит')
else:
    print('не подходит')
