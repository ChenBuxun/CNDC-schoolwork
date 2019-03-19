# last modified 20th Mar, from Lynne
import socket

s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.connect(('169.254.159.1',12000))

sentence = input("input lowercase sentence:")
s0.send(sentence.encode())

modifiedSentence = s0.recv(1024)
print("From Server:", modifiedSentence.decode())

s0.close()
