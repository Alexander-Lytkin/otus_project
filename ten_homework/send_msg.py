import socket

with socket.socket() as s:
    s.connect(('', 4890))
    while True:
        text = input(f"Введите запрос: ")
        print(f'Sending message\n"{text}"')
        sent_bytes = s.send(text.encode('utf-8'))
        print(f'{sent_bytes} bytes sent')
        # if text == "выход":
        # break
        # conn, raddr = s.accept()
        # data = conn.recv(1024)
        # text = data.decode('utf-8')
        # print(data)
    s.close()
    