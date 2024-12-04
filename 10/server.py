import threading
import random
import time


class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.lock = threading.Lock()  # Используем блокировку для синхронизации доступа к ресурсам

    def park_car(self, car_id):
        with self.lock:  # Защищаем доступ к общему ресурсу
            if self.available_spots > 0:
                self.available_spots -= 1
                print(f"Автомобиль {car_id} заехал на парковку. Свободные места: {self.available_spots}")
                return True
            else:
                print(f"Автомобиль {car_id} не смог заехать, парковка полна.")
                return False

    def leave_parking(self, car_id):
        with self.lock:  # Защищаем доступ к общему ресурсу
            self.available_spots += 1
            print(f"Автомобиль {car_id} покинул парковку. Свободные места: {self.available_spots}")


def car(parking_lot, car_id):
    # Попытка заехать на парковку
    if parking_lot.park_car(car_id):
        # Имитация времени, проведенного на парковке
        parking_time = random.randint(1, 5)  # Автомобиль проводит от 1 до 5 секунд на парковке
        time.sleep(parking_time)
        # Выезд с парковки
        parking_lot.leave_parking(car_id)


def main():
    total_spots = 2  # Общее количество мест на парковке
    parking_lot = ParkingLot(total_spots)

    # Создаем и запускаем потоки для автомобилей
    threads = []
    for car_id in range(10):
        thread = threading.Thread(target=car, args=(parking_lot, car_id))
        threads.append(thread)
        thread.start()
        time.sleep(random.randint(1, 3))  # Имитация случайного времени между прибытием автомобилей

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
