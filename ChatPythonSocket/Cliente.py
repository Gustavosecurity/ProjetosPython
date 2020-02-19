import socket

IP_Cliente = "127.0.0.1"
PORT_Ciente = 7000

cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = ((IP_Cliente, PORT_Ciente))
cliente.connect(orig)
while True:

    msg = input('Digite uma msg')
    cliente.send(msg.encode('utf-8'))

cliente.close()