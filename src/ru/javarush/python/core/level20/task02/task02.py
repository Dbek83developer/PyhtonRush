# Ханойские башни

# Задача о Ханойских башнях. Напиши функцию, которая возвращает количество перемещений дисков, если всего дисков n.


def hanoi_moves(n):
    if n == 1:
        return 1
    return 2 * hanoi_moves(n - 1) + 1

# Пример использования
n = 4
print(hanoi_moves(n))  # Вывод: 15