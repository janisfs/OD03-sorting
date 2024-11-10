# Функция merge_sort принимает массив arr в качестве аргумента
def merge_sort(arr):
    # Если длина массива меньше или равна 1, то он уже отсортирован
    if len(arr) <= 1:
        return arr  # Возвращаем исходный массив

    # Разбиваем массив на две части: left_half и right_half
    mid = len(arr) // 2  # Находим середину массива
    left_half = arr[:mid]  # Левая половина массива
    right_half = arr[mid:]  # Правая половина массива

    # Рекурсивно сортируем обе части
    left_half = merge_sort(left_half)  # Сортируем левую половину
    right_half = merge_sort(right_half)  # Сортируем правую половину

    # Объединяем отсортированные части
    return merge(left_half, right_half)  # Вызываем функцию merge

# Функция merge принимает две отсортированные части в качестве аргументов
def merge(left, right):
    # Создаем пустой массив для хранения объединенного результата
    merged = []
    left_index = 0  # Индекс для левой части
    right_index = 0  # Индекс для правой части

    # Объединяем части, пока не достигнем конца одной из них
    while left_index < len(left) and right_index < len(right):
        # Сравниваем текущие элементы левой и правой частей
        if left[left_index] <= right[right_index]:
            # Если элемент левой части меньше или равен, добавляем его в merged
            merged.append(left[left_index])
            left_index += 1  # Переходим к следующему элементу левой части
        else:
            # Если элемент правой части меньше, добавляем его в merged
            merged.append(right[right_index])
            right_index += 1  # Переходим к следующему элементу правой части

    # Добавляем оставшиеся элементы левой или правой части в merged
    merged.extend(left[left_index:])  # Добавляем оставшиеся элементы левой части
    merged.extend(right[right_index:])  # Добавляем оставшиеся элементы правой части

    return merged  # Возвращаем объединенный результат

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)