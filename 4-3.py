# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from source import polynomial
a = (int(input ("Введите натуральную степень: ")))
file1 = open ('4-3.txt', 'w')
file1.write (polynomial(a,2))
file1.close()