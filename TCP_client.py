import socket
import sys

target_host = "0.0.0.0"
target_port =  9999

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send data
client.send(sys.argv[1])

#recive data
responce = client.recv(4096)

print responce