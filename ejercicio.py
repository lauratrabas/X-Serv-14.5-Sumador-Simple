#!/usr/bin/python

#Laura Trabas Clavero

import socket
import random

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
		entero = peticion.split()[1][1:]
	except KeyError:
		continue
	
	if numero == True:
		numero1 = int(entero)
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("El primer numero es:" + str(numero1))
		recvSocket.send("<html><body><h1>" + "Introduzca su segundo numero ")
		recvSocket.send("</h1></body></html>")
		numero = False
	else:
		resultado = numero1 + int(entero)
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("</body></html>")
		recvSocket.send(str(numero1) +  str(entero))
		recvSocket.send("El resultado es:" + str(resultado))
		recvSocket.send("<html><body><h1>" + "\r\n")
		numero = True
	recvSocket.close()

mySocket.close()

