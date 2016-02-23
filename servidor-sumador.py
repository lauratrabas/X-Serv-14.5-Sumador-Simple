
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

numero = True

while True:
	print 'Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print 'HTTP request received'
	peticion = recvSocket.recv(1301)
	try:
		entero = int(peticion.split()[1][1:])
	except KeyError:
		continue
	
	if numero == True:
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("<html><body>")
		recvSocket.send('El primer numero es: </p>' + str(entero))
		recvSocket.send('<p>Introduzca su segundo numero')
		recvSocket.send("</body><html>" + "\r\n")
		numero1 = entero
		numero = False
	else:
		suma = numero1 + entero
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("<body><html>")
		recvSocket.send(str(numero1) + '+' + str(entero) + '</p>')
		recvSocket.send('El resultado es:</p>' + str(suma))
		recvSocket.send("</body><html>" + "\r\n")
		numero = True
	recvSocket.close()

mySocket.close()

