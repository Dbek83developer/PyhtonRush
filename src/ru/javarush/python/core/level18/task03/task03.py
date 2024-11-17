# Рекурсивный поиск

# Напишите рекурсивный алгоритм для проверки, присутствует ли определённое значение в отсортированном массиве строк.


def recursive_search(arr, target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return recursive_search(arr, target, left, mid - 1)
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, right)
    else:
        return False

def is_value_present(arr, target):
    return recursive_search(arr, target, 0, len(arr) - 1)

# Пример использования:
arr = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
target = "cherry"
print(is_value_present(arr, target))  # Output: True

target = "mango"
print(is_value_present(arr, target))  # Output: False