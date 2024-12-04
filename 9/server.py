import threading
import math

# Список для хранения результатов
results = []


def calculate_factorial(n):
    """Вычисление факториала числа n."""
    try:
        if n < 0:
            raise ValueError("Факториал не определен для отрицательных чисел.")
        result = math.factorial(n)
        results.append(f"Факториал {n} = {result}")
    except Exception as e:
        results.append(f"Ошибка при вычислении факториала {n}: {e}")


def calculate_power(base, exponent):
    """Вычисление возведения числа base в степень exponent."""
    try:
        result = base ** exponent
        results.append(f"{base} в степени {exponent} = {result}")
    except Exception as e:
        results.append(f"Ошибка при вычислении {base} в степени {exponent}: {e}")


def calculate_integral(func, lower_limit, upper_limit, num_steps=1000):
    """Вычисление определенного интеграла функции func от lower_limit до upper_limit."""
    try:
        step = (upper_limit - lower_limit) / num_steps
        integral_value = 0
        for i in range(num_steps):
            x = lower_limit + i * step
            integral_value += func(x) * step
        results.append(f"Интеграл от функции на отрезке [{lower_limit}, {upper_limit}] = {integral_value}")
    except Exception as e:
        results.append(f"Ошибка при вычислении интеграла: {e}")


def main():
    # Запускаем вычисления в отдельных потоках
    threads = [threading.Thread(target=calculate_factorial, args=(5,)),
               threading.Thread(target=calculate_power, args=(2, 10)),
               threading.Thread(target=calculate_integral, args=(lambda x: x ** 2, 0, 1))]

    # Запускаем потоки
    for thread in threads:
        thread.start()

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()

    # Выводим результаты
    print("\nРезультаты вычислений:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
