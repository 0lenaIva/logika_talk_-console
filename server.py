import socket
import time
import threading

HOST='localhost'
PORT=8080
users = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('очікуємо клієнта')

def broadcast(message):
    for client in users:
        try:
            client.send(f'{message}'.encode())
        except:
            pass

def handle_client(client):
    userName = client.recv(1024).decode().strip()
    broadcast(f'{userName} доєднався!')
    while True:
        try:
            message = client.recv(1024).decode().strip()
            broadcast(f'{userName}: {message}')
        except:
            users.remove(client)
            broadcast(f'{userName} відключився')
            client.close()
            break

while True:#<--------------------------------

    client, address = server_socket.accept()
    users.append(client)
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
        

    

    


    
    


