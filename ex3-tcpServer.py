# last modified 20th Mar, from Lynne

import socket
serverPort = 12000
s1= socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('169.254.159.1',serverPort))
s1.bind(('localhost',serverPort))
s1.listen(2)
print ("The server is ready to receive")

while True:
    connectionSocket, addr = s1.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()