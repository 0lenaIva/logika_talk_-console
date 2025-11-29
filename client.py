import socket
import threading

HOST='7.tcp.eu.ngrok.io'
PORT = 18093

name = input('ВВедіть ім\'я: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
    client_socket.send(name.encode())

except:
    print('підключення не вдалось')



def send_message():
    while True:
        try:
            message = input('>>> ')
            client_socket.send(message.encode())
        except:
            pass

threading.Thread(target=send_message).start()


while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
    except:
        print('роз\'єдналось з\'єднання')
        break

client_socket.close()