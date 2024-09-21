# Разность множеств
import random
# Напишите программу, которая создает два множества из случайных чисел.
# Первое множество содержит 10 случайных чисел в диапазоне от 1 до 20, а второе множество содержит 10 случайных чисел в диапазоне от 10 до 30.
# Программа должна найти разность первого множества со вторым с использованием метода difference().
# И симметрическую разность с использованием метода symmetric_difference().
# Программа должна вывести оба результата.

# Напишите тут ваш код
set1 = set([random.randint(1, 20) for _ in range(10)])
set2 = set([random.randint(10, 30) for _ in range(10)])
diff = set1.difference(set2)
print(diff)
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
