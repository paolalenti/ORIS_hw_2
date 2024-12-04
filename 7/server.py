import threading
from collections import Counter
import os


def count_word_frequency(file_part, result, index):
    """Функция для подсчета частоты слов в части файла."""
    word_freq = Counter()
    with open(file_part, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            word_freq.update(words)
    result[index] = word_freq


def merge_results(results):
    """Функция для объединения результатов из всех потоков."""
    merged_result = Counter()
    for result in results:
        merged_result.update(result)
    return merged_result


def split_file(file_path, num_parts):
    """Функция для разбивки файла на равные части."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    part_size = len(content) // num_parts
    parts = []
    for i in range(num_parts):
        start_index = i * part_size
        end_index = None if i == num_parts - 1 else (i + 1) * part_size
        parts.append(content[start_index:end_index])

    # Записываем части во временные файлы
    part_files = []
    for i, part in enumerate(parts):
        part_file = f'part_{i}.txt'
        with open(part_file, 'w', encoding='utf-8') as f:
            f.writelines(part)
        part_files.append(part_file)

    return part_files


def main(file_path, num_threads):
    # Разбиваем файл на части
    part_files = split_file(file_path, num_threads)

    threads = []
    results = [None] * num_threads

    # Создаем и запускаем потоки
    for i in range(num_threads):
        thread = threading.Thread(target=count_word_frequency, args=(part_files[i], results, i))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    # Объединяем результаты
    final_result = merge_results(results)

    # Выводим итоговую статистику
    for word, count in final_result.most_common(10):  # Выводим 10 самых частых слов
        print(f"{word}: {count}")

    # Удаляем временные файлы
    for part_file in part_files:
        os.remove(part_file)


if __name__ == "__main__":
    file_path = 'word.txt'
    num_threads = 4

    main(file_path, num_threads)