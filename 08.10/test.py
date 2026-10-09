import numpy as np

print("Calculator project is running!")

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Первый массив:", a)
print("Второй массив:", b)

print("Сложение:", a + b)
print("Вычитание:", a - b)
print("Умножение:", a * b)
print("Деление:", a / b)

print("Среднее значение:", np.mean(a))