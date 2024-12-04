import os
import fnmatch
import threading


def find_files(pattern, directory, results, lock, semaphore):
    """Функция для поиска файлов по заданному паттерну в указанной директории."""
    with semaphore:  # Ограничиваем количество одновременно работающих потоков
        print(f"Searching in directory: {directory}")
        matches = []
        for root, dirnames, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))

        # Используем блокировку для безопасного добавления результатов
        with lock:
            results.extend(matches)


def main(directories, pattern, max_threads):
    results = []
    lock = threading.Lock()
    semaphore = threading.Semaphore(max_threads)  # Создаем семафор для ограничения потоков
    threads = []

    for directory in directories:
        # Создаем и запускаем новый поток для поиска
        thread = threading.Thread(target=find_files, args=(pattern, directory, results, lock, semaphore))
        thread.start()
        threads.append(thread)

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    return results


if __name__ == "__main__":
    # Список каталогов для поиска
    directories = [
        '1',
        '2',
        '3'
    ]

    # Паттерн для поиска
    pattern = '*.png'

    # Максимальное количество потоков
    max_threads = 2

    found_files = main(directories, pattern, max_threads)

    # Выводим итоговые результаты
    print("\nAll found files:")
    for file in found_files:
        print(file)
