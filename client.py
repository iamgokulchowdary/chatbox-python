import threading
import socket

serverip = "10.97.43.81"
port = 9999
serveraddress = (serverip,port)

client = socket.socket()
client.connect(serveraddress)

nickname = input("Enter your Nickname : ")

client.send(nickname.encode("ascii"))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Error occured...")
            break

def send():
    while True:
        message = input("")
        client.send(message.encode("ascii"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
