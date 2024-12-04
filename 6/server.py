import socket
import threading


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                return False, self.balance
            self.balance -= amount
            return True, self.balance

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            return self.balance


class BankServer:
    def __init__(self, host='localhost', port=65432, initial_balance=1000):
        self.bank_account = BankAccount(initial_balance)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        print(f"Сервер запущен на {host}:{port}")

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            command, amount = data.split()
            amount = int(amount)

            if command == 'withdraw':
                success, balance = self.bank_account.withdraw(amount)
                if success:
                    response = f"Снято {amount}. Новый баланс: {balance}"
                else:
                    response = f"Недостаточно средств. Текущий баланс: {balance}"
            elif command == 'deposit':
                balance = self.bank_account.deposit(amount)
                response = f"Внесено {amount}. Новый баланс: {balance}"

            client_socket.send(response.encode())

        client_socket.close()

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Принято соединение от {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()


if __name__ == "__main__":
    server = BankServer()
    server.start()