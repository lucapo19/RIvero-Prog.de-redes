import socket
host = "localhost"
port = 5656
objcliente=socket.socket(socket.AF_INET, socket.SOCK_STREAN)
objcliente.connect((host,port))
print ("el cliente se ha iniciado")

while true:
enviar= input("cliente: ")
objcliente.send (enviar.encode(encoding="ascii", errors="ignore"))+
recibido = objcliente.recv(1024)
print ("servidor", recibido.decode(encoding="ascii" , errors="ignore"))
objcliente.close () 