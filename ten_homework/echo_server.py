import socket
from http import HTTPStatus

from ten_homework.helper import get_open_port

HOST = "localhost"
PORT = get_open_port()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Старт сервера на {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen(1)
    
    while True:
        print('Ожидание соединения...')
        conn, address = s.accept()
        print("Подключено к:", address)
        
        data = conn.recv(1024)
        print(f"Получено: \n{data}\n")
        data = data.decode("utf-8").strip()
        
        status_value = 200
        status_phrase = "OK"
        if data:
            try:
                print('Обработка данных...')
                status = data.split()[1].split("/?status=")
                if len(status) == 2:
                    status_code = int(status[1].split()[0])
                    stat = HTTPStatus(status_code)
                    status_value = status_code
                    status_phrase = stat.phrase
            except (ValueError, IndexError):
                pass
            
            # Тело ответа
            resp = "\r\n".join(data.split("\r\n")[1:])
            body = "\r\n".join([
                f"Request Method: {data.split()[0]}",
                f"Request Source: {address}",
                f"Response Status: {status_value} {status_phrase}",
                resp
            ])
            # Заголовки ответа
            status_line = f"{data.split()[2]} {status_value} {status_phrase}"
            headers = "\r\n".join([
                status_line,
                f"Content-Type: text/plain",
                f"Content-Length: {len(body)}"
            ])
            # Ответ от сервера
            message = "\r\n\r\n".join([
                headers,
                body
            ]).encode("utf-8")
            
            print('Отправка обратно клиенту.')
            conn.send(message)
        else:
            print('Нет данных от:', address)
            break
        # Очищаем соединение
        conn.close()
