import socket
import threading
from gameclass import *
import pickle
import random


host = 'localhost'
port = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

objectList = {}
playerNo = 0

server.listen()

def handleClient(conn,playerno):

    userName = conn.recv(100).decode()

    print(userName)

    objectList[playerno]=Player(random.randint(0,700),random.randint(0,700),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),10,10,50,userName)

    print(objectList[playerno])

    conn.send(pickle.dumps(objectList[playerno]))

    while True:
        
        objectList[playerno]=pickle.loads(conn.recv(5000))

        objectList[playerno]

        if objectList[playerno] == False:

            conn.close()
            del objectList[playerno]
            break

        temp = objectList.copy()
        temp.pop(playerno)

        conn.send(pickle.dumps(list(temp.values())))

while True:

    conn, addr = server.accept()

    thread = threading.Thread(target=handleClient,args=(conn,playerNo))
    thread.start()

    playerNo += 1