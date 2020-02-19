import socket

IP_Serve = "127.0.0.1"
PORT_Serve = 7000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = ((IP_Serve, PORT_Serve))
servidor.bind(orig)
servidor.listen(5)

print('Esperando coneçao......')
dados, cliente = servidor.accept()
print('conectado a ', cliente)

while True:
    msg = dados.recv(1024)
    texto = msg.decode('utf-8')
    print('mensagem recebida -> ', msg)


servidor.close
