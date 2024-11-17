# Урановые ломы в ртути

# Напишите функцию, которая использует сортировку пузырьком для сортировки списка чисел по убыванию.


def sort_desc_bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
numbers = [5, 3, 8, 4, 2]
sorted_numbers = sort_desc_bubble(numbers)
print(sorted_numbers)  # Вывод: [8, 5, 4, 3, 2]