import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.182.206',9090))
sock.listen()
while True:
    conn,addr = sock.accept()
    print(conn,addr)
