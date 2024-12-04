import socket


class BankClient:
    def __init__(self, host='localhost', port=65432):
        # Инициализация клиента и подключение к серверу
        self.server_address = (host, port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

    def withdraw(self, amount):
        # Метод для снятия денег
        request = f"withdraw {amount}"
        self.client_socket.send(request.encode())
        response = self.client_socket.recv(1024).decode()
        print(response)

    def deposit(self, amount):
        # Метод для внесения денег
        request = f"deposit {amount}"
        self.client_socket.send(request.encode())
        response = self.client_socket.recv(1024).decode()
        print(response)

    def close(self):
        # Закрытие сокета клиента
        self.client_socket.close()


if __name__ == "__main__":
    client = BankClient()

    while True:
        print("\nВыберите действие:")
        print("1. Снять деньги")
        print("2. Пополнить счет")
        print("3. Выход")

        choice = input("Введите номер действия (1/2/3): ")

        if choice == '1':
            amount = int(input("Введите сумму для снятия: "))
            client.withdraw(amount)
        elif choice == '2':
            amount = int(input("Введите сумму для пополнения: "))
            client.deposit(amount)
        elif choice == '3':
            print("Выход из клиента.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    client.close()