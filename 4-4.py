# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

x = (int(input("Введите первое число: ")))
y = (int(input("Введите второе число: ")))
if x > y:
    max_num = x
else:
    max_num = y
while (True):
    if (max_num % x == 0) and (max_num % y == 0):
        result = max_num
        break
    max_num += 1
print(result)
