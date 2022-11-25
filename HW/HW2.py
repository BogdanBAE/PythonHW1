# 2'. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

print('Введите X ')
x = int(input())
print('Введите Y ')
y = int(input())
print('Введите Z ')
z = int(input())

if ((not (x or y or z)) == ((not x) and (not y) and (not y))):
    print('True')
else:
    print('False')
