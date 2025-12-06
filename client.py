import socket
import threading
from colorama import Fore, Style, init
from pyfiglet import Figlet
from time import sleep

init()

fig = Figlet(font='slant')# big banner3-D standard

HOST = '6.tcp.eu.ngrok.io'
PORT = 13861

name = input('Введіть ім\'я: ')
print(fig.renderText('LOGIKA TALK'))

def type_writer(text, color = Fore.GREEN, delay = 0.02):
    for char in text:
        print(color + char + Style.RESET_ALL, end='', flush = True)
        sleep(delay)
    print()

client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

try:
    client_socket.connect((HOST,PORT))
    client_socket.send(name.encode())
except:
    print(Fore.RED + 'підключення не вдалось.' + Style.RESET_ALL)

def send_message():
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            print(Fore.RED + 'помилка з сервером' + Style.RESET_ALL)

threading.Thread(target=send_message).start()

while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            type_writer(message, Fore.GREEN, 0.01)
    except:
        type_writer('Роз\'єдналось з\'єднання', Fore.RED, 0.01)
        break

client_socket.close()
