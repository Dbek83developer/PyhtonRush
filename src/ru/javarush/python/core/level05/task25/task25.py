# Добавление элемента

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя новый элемент и добавить его в конец кортежа, создавая новый кортеж.
# Программа должна вывести обновленный кортеж.

# Напишите тут ваш код
alist = [input("Enter: ") for _ in range(5)]
element = input("Enter new element: ")
kortej = tuple(alist)
alist.append(element)
new_kortej = tuple(alist)
print(new_kortej)
