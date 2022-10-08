# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from source import create_list_int as cl

lst = cl()
result = []
for i in range(len(lst) // 2 + len(lst) % 2):
    result.append((lst[i]) * (lst[-(i + 1)]))
print(result)
