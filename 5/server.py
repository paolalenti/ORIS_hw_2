import threading
import random

def sort_subarray(arr, start, end, result, index):
    """Сортирует подмассив и сохраняет результат."""
    result[index] = sorted(arr[start:end])

def merge_sorted_arrays(arr1, arr2):
    """Объединяет два отсортированных массива в один отсортированный массив."""
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Добавляем оставшиеся элементы
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def threaded_sort(arr, num_threads):
    """Сортирует массив с использованием потоков."""

    # Разделяем массив на подмассивы
    length = len(arr)
    subarray_length = length // num_threads
    threads = []
    result = [None] * num_threads

    for i in range(num_threads):
        start = i * subarray_length
        # Обрабатываем последний подмассив отдельно
        end = start + subarray_length if i < num_threads - 1 else length
        thread = threading.Thread(target=sort_subarray, args=(arr, start, end, result, i))
        threads.append(thread)
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Объединяем отсортированные подмассивы
    sorted_array = result[0]
    for i in range(1, len(result)):
        sorted_array = merge_sorted_arrays(sorted_array, result[i])

    return sorted_array

def main():
    # Генерируем случайный массив чисел
    array_size = 100 # Размер массива
    num_threads = 3     # Количество потоков
    random_array = [random.randint(1, 1000) for _ in range(array_size)]

    print("Исходный массив:", random_array)
    sorted_array = threaded_sort(random_array, num_threads)
    print("Отсортированный массив:", sorted_array)

if __name__ == "__main__":
    main()