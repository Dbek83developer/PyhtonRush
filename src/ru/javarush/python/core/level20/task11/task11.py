# Поиск по базе

# Есть база данных состоящая из миллиарда записей.
# Вам нужно выбрать алгоритм, который лучше подойдет для поиска в такой базе.
# Нужно найти запись в отсортированной базе данных. Используйте правильный алгоритм.
# Подсказка:
# Можете просто вызвать готовый, писать с нуля не обязательно


import bisect


def search(sorted_db, target):
    index = bisect.bisect_left(sorted_db, target)
    if index < len(sorted_db) and sorted_db[index] == target:
        return index
    return -1


# Пример использования
sorted_db = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = search(sorted_db, target)
print("Запись найдена на индексе:", result)