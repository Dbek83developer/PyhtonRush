# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более глубокого уровня вложенности.
# Добавить новый элемент в вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

# Напишите тут ваш код
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    },
    "contact": {
        "phone": "1233-345-998",
        "email": "dbek.developer@gmail.com"
                }
}


person["name"] = "Mike"
person["address"]["zip"] = "10002"
person["address"]["province"] = "DC Washington"
del person["city"]
del person["contact"]["email"]
print(person)

