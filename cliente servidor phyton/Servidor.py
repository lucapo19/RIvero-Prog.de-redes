import socket
host = "localhost"
port = 5066
servidor=socket.socket(socket.AF_INFT, socket.SOCK_STREAM)
servidor.bind((host,port))
servidor.listen(1)
print ("servidor esperando conexion")
active, addr= servidor.accept()

while true:
recibido=active.recv(1024)
print ("cliente: ", recibido.decode(encoding="ascii", errors="ignore"))
enviar=input ("server: ")
active.send(enviar.encode(encoding="ascii", errors="ignore"))
active.close()
