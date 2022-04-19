import socket
from helper import get_open_port
# создаемTCP/IP сокет
from http import HTTPStatus

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = get_open_port()
# Привязываем сокет к порту
server_address = ('localhost', port)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    print('Подключено к:', client_address)
    # Принимаем данные порциями и ретранслируем их
    while True:
        data = connection.recv(1024)
        print(f'Получено: {data.decode()}')
        
        status_value = 200
        status_name = "OK"
        
        if data:
            print('Обработка данных...')
            text = data.decode('utf-8')
            try:
                status = text.split()[1]
                if status.isdigit() and status != " " or status == "/":
                    status_value, status_name = HTTPStatus(int(status)).value, HTTPStatus(int(status)).name
            except (ValueError, IndexError):
                pass
        
            data = data.split()[2].decode('utf-8')
            status_line = f"{data} {status_value} {status_name}"
            print('Отправка обратно клиенту.')
            body = '<h1>Hello from OTUS!</h1>'
            headers = '\r\n'.join([
                status_line,
                'Content-Type: text/html; charset=UTF-8',
                f'Content-Length: {len(body)}'
            ])
            resp = '\r\n\r\n'.join([
                headers,
                body
            ])
            
            sent_bytes = connection.send(
                    resp.encode("utf-8")
                )
        else:
            print('Нет данных от:', client_address)
            break
            # Очищаем соединение
            connection.close()
