# Обратный кортеж

# Напишите программу, которая создает кортеж из произвольного количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести кортеж в обратном порядке с использованием среза.

# Напишите тут ваш код
alist = []
while True:
    item = input("add: ")
    if len(item) == 0:
        break
    else:
        alist.append(item)
my_tuple = tuple(alist)

# if len(my_tuple) == 0:
#     print("Tuple empty")
# else:
#     print(my_tuple[-1])

print(my_tuple[::-1])