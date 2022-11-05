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

print('server started')

def handleClient(conn,playerno):



    try:
        userName = conn.recv(100).decode()
        objectList[playerno]=Player(random.randint(0,700),random.randint(0,700),(random.randint(60,255),random.randint(60,255),random.randint(60,255)),7,6,60,userName)
        conn.send(pickle.dumps(objectList[playerno]))
        print(f'{userName} connected')

    except:
        pass

    while True:
        
        try:
            objectList[playerno]=pickle.loads(conn.recv(5000))
            if objectList[playerno] == False:

                conn.close()
                del objectList[playerno]

                break

            temp = objectList.copy()
            temp.pop(playerno)

            conn.send(pickle.dumps(list(temp.values())))
        except:
            conn.close()
            del objectList[playerno]
            break

while True:

    conn, addr = server.accept()

    thread = threading.Thread(target=handleClient,args=(conn,playerNo))
    thread.start()
    

    playerNo += 1
