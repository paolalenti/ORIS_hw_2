import threading

def is_prime(num):
    """Проверка, является ли число простым."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end, result):
    """Поиск простых чисел в заданном диапазоне."""
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

def main():
    # Ввод диапазона от пользователя
    start_range = int(input("Введите начальное значение диапазона: "))
    end_range = int(input("Введите конечное значение диапазона: "))
    num_threads = int(input("Введите количество потоков: "))

    # Разделение диапазона на части
    step = (end_range - start_range) // num_threads
    threads = []
    results = [[] for _ in range(num_threads)]

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range
        thread = threading.Thread(target=find_primes_in_range, args=(start, end, results[i]))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Объединение результатов
    all_primes = []
    for result in results:
        all_primes.extend(result)

    print(f"Простые числа в диапазоне от {start_range} до {end_range}: {sorted(all_primes)}")

if __name__ == "__main__":
    main()