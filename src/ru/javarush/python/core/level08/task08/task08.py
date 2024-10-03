# Генератор выражений.

# Напишите программу, которая использует генераторное выражение для создания
# последовательности квадратов чисел от 1 до 10. Программа должна:
# Создать генераторное выражение для генерации квадратов чисел.
# Использовать этот генератор для вывода всех значений последовательности.

# Напишите тут ваш код
squares = (x ** 2 for x in range(1, 11))
for _ in range(10):
    print(next(squares))
