import threading
from socket import *
serverPort = 12010
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)


def fun_rec(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode() #Fill in start  #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        http_header = 'HTTP/1.1 200 OK\nConnection:Close\n' \
                      'Content-Type:text/html\nContent-Length:%d\n\n' % (len(outputdata))
        connectionSocket.send(http_header.encode('utf8'))
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf8'))
        connectionSocket.close()
    except IOError as e:
        print(e)
        #Send response message for file not found
        #Fill in start
        http_header = 'HTTP/1.1 404 Found\n'
        connectionSocket.send(http_header.encode('utf8'))
        #Fill in end
        connectionSocket.close()
        #Fill in start
        #Fill in end


while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in start  #Fill in end
    thing = threading.Thread(target=fun_rec, args=(connectionSocket,))
    thing.start()
serverSocket.close()
