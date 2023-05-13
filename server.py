import threading
import socket

serverip = "localhost"
port = 9999
serveraddress = (serverip,port)

server = socket.socket()
server.bind(serveraddress)
print("server started...")

server.listen()
print("server is listining...")

clients = []
nicknames = []

def broadcast(message,nickname=""):
    for client in clients:
        client.send(f"{nickname} : {message}".encode("ascii"))

def handle(client,nickname):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message,nickname)       
        except:
            clients.remove(client)
            client.close()

            broadcast(f"{nickname} left the chat")
            nicknames.remove(nickname)
            break
            

while True:
    client,address = server.accept()
    print(f"{address} is connected to server")

    nickname = client.recv(1024).decode()
    print(f"{address} is {nickname}")
    client.send("Your are connected...".encode("ascii"))
    broadcast(f"{nickname} joined the chat")

    clients.append(client)
    nicknames.append(nickname)

    threading.Thread(target=handle, args=(client,nickname)).start()