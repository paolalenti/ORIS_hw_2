import socket
import threading


def handle_client(client_socket, addr):
    print(f"Подключен клиент: {addr}")

    # Запрос имени потока
    client_socket.send("Введите имя потока: ".encode('utf-8'))
    thread_name = client_socket.recv(1024).decode('utf-8')
    print(f"Поток с именем '{thread_name}' подключен.")

    while True:
        # Ожидание команды от клиента
        command = client_socket.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            print(f"Поток '{thread_name}' отключен.")
            break
        # Игнорируем все остальные команды
        print(f"Игнорируем команду от потока '{thread_name}': {command}")

    client_socket.close()


def start_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязка сокета к адресу и порту
    server_socket.bind(('localhost', 12345))

    # Начало прослушивания входящих соединений
    server_socket.listen(5)
    print("Сервер запущен. Ожидание подключений...")

    while True:
        # Принятие соединения
        client_socket, addr = server_socket.accept()
        # Создание потока для обработки клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()