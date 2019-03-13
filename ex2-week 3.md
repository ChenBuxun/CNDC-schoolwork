Week 3 assignment


- ![Image text](/img/2-0.JPG)
- ![Image text](/img/2-1.JPG)

I bet nothing wrong with my password...?



**P1** 

a) F, there'll be 4 request messages

b) T, they're sent to the same server

c) F, in non-persistent connections, no

d) F, it's when the message is sent

e) F

**P3**

app: DNS to get ip address, HTTP to manage messages

trans: UDP/ TCP

**P4**

a) www.gaia.cs.umass.edu/cs453/index.html

b) 1.1

c) consistent

d) unknown

e) Mozilla/5.0, server can thus send different versions of the objects

**P7**

2RTT₀ (HTTP)+ RTT₁+... RTTn (DNS)

**P12**

`from socket import *`

`serverPort= 12000`

`serverSocket= socket( AF_INET, SOCK_STREAM)`

`serverSocket. bind((' ', serverPort))`

`serverSocket.listen(1)`

`while True:`

​    `connectionSocket, addr= serverSocket.accept()`

​    `sentence= connectionSocket. recv(1024).decode()`

​    `print(sentence, '\n')`

​    `connectionSocket.close()`

`serverSocket.close()`
