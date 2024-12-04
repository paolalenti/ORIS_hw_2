import threading


def partial_factorial(start, end, result, index):
    """Вычисление частичного факториала от start до end."""
    partial_result = 1
    for i in range(start, end + 1):
        partial_result *= i
    result[index] = partial_result


def factorial(n, num_threads):
    """Вычисление факториала числа n с использованием num_threads потоков."""
    if n == 0 or n == 1:
        return 1

    # Разделение диапазона на части
    step = n // num_threads
    threads = []
    results = [1] * num_threads  # Список для хранения частичных результатов

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i < num_threads - 1 else n
        thread = threading.Thread(target=partial_factorial, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Вычисление окончательного результата
    final_result = 1
    for res in results:
        final_result *= res

    return final_result


def main():
    n = int(input("Введите число для вычисления факториала: "))
    num_threads = int(input("Введите количество потоков: "))

    result = factorial(n, num_threads)
    print(f"Факториал числа {n} равен {result}")


if __name__ == "__main__":
    main()
