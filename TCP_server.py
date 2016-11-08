import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)
print  "[*] Listening on %s:%d " % (bind_ip,bind_port)

#Client Handler Thread
def handle_client(client_socket):
    #print out what client sends
    request = client_socket.recv(1024)

    print "[*] Reveived: %s " % request

    #send back a package
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client, addr = server.accept()

    print "[*] Accepted connections from %s:%d " % (addr[0], addr[1])

    #sping up the client thread to handle incoming data#
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()