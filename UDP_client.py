import socket

target_host = "0.0.0.0"
target_port = 9999

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect the client
client.sendto("AAAABBBBCCCC", (target_host,target_port))

#recive data
data, responce = client.recvfrom(4096)

print data