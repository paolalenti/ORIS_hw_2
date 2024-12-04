import socket


def start_client():
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    client_socket.connect(('localhost', 12345))

    # Получение запроса на имя потока
    prompt = client_socket.recv(1024).decode('utf-8')
    print(prompt)

    # Ввод имени потока
    thread_name = input()
    client_socket.send(thread_name.encode('utf-8'))

    while True:
        command = input("Введите команду (или 'exit' для выхода): ")
        client_socket.send(command.encode('utf-8'))
        if command.lower() == 'exit':
            break

    client_socket.close()


if __name__ == "__main__":
    start_client()