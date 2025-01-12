# Подбор хеш-функции

# У нас есть дни рождения людей заданные как (день, месяц, год).
# Придумайте такую хеш-функцию, чтобы они распределялись максимально равномерно.


def custom_hash(day, month, year):
    return (day + month * 31 + year * 31 * 12) % 10007

# Пример использования:
birthdays = [
    (1, 1, 1990),
    (15, 10, 1985),
    (23, 7, 2000),
    (11, 12, 1965),
    (5, 5, 2010)
]

hashed_values = [custom_hash(day, month, year) for day, month, year in birthdays]
print(hashed_values)