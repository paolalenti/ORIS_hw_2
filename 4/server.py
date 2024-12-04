import threading

def fibonacci_worker(n, results, index):
    """Функция для вычисления n-го числа Фибоначчи."""
    if n <= 1:
        results[index] = n
    else:
        # Вычисляем n-1 и n-2 в отдельных потоках
        results[index] = fibonacci(n)

def fibonacci(n):
    """Вычисление n-го числа Фибоначчи."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_with_threads(n):
    """Вычисление n-го числа Фибоначчи с помощью потоков."""
    if n <= 1:
        return n, n, n  # Возвращаем n, n-1 и n-2

    # Список для хранения результатов
    results = [0, 0]  # Для n-1 и n-2
    threads = []

    # Создаем потоки для вычисления n-1 и n-2
    for i in range(2):  # два потока
        thread = threading.Thread(target=fibonacci_worker, args=(n - i - 1, results, i))
        threads.append(thread)
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Объединяем результаты
    return results[0] + results[1], results[0], results[1]  # Возвращаем n, n-1 и n-2

def main():
    n = int(input("Введите номер числа Фибоначчи для вычисления: "))
    result, fib_n_minus_1, fib_n_minus_2 = fibonacci_with_threads(n)
    print(f"Fibonacci({n}) = {result}")
    print(f"Fibonacci({n-1}) = {fib_n_minus_1}")
    print(f"Fibonacci({n-2}) = {fib_n_minus_2}")

if __name__ == "__main__":
    main()