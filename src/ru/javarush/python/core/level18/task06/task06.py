# Количество путей

# Напишите функцию для вычисления количества различных путей из верхнего левого угла сетки размером m x n
# в нижний правый угол, используя мемоизацию для оптимизации.

def count_paths(m, n, i, j, memo):
    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]

    memo[(i, j)] = count_paths(m, n, i + 1, j, memo) + count_paths(m, n, i, j + 1, memo)
    return memo[(i, j)]


def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0

    # Запуск рекурсивной функции с начальной точки (0, 0)
    return count_paths(m, n, 0, 0, {})

# Примеры использования
print(unique_paths(3, 7))  # Ожидаемый результат: 28
print(unique_paths(3, 3))  # Ожидаемый результат: 6
print(unique_paths(1, 1))  # Ожидаемый результат: 1
print(unique_paths(0, 0))  # Ожидаемый результат: 0