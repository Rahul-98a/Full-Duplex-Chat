from socket import *
import sys
import threading


# function for receiving message from client
def send_to_server(clsock):
    while True:
        send_msg = input('Type Message: ')
        clsock.sendall(send_msg.encode())


# function for receiving message from client
def recv_from_server(conn):
    global FLAG
    while True:
        # Receives the request message from the client
        message = conn.recv(1024).decode()
        # if 'q' is received from the client the server quits
        if message == 'q':
            conn.send('q'.encode())
            print('Closing connection')
            conn.close()
            FLAG = True
            print('Message Received: ' + message)	
        if message != False:
           print('Message Received: ' + message)
           


# this is main function
def main():
    # TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
    HOST = 'localhost'
    # TODO (2) - define PORT number (1 line) (Google, what should be a valid port number) 
    PORT = 65535
    PORT2 = 65534

    # Create a TCP client socket
	#(AF_INET is used for IPv4 protocols)
	#(SOCK_STREAM is used for TCP)
    # TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket2 = socket(AF_INET, SOCK_STREAM)

    # bind socket
    clientSocket2.bind(('', PORT2))
    clientSocket.connect((HOST, PORT))

	# listen to for server and wait for request
    clientSocket2.listen(1)
    clientconnection, addr = clientSocket2.accept()

    # request to connect sent to server defined by HOST and PORT
    # TODO (4) - request a connection to the server (1 line)
    print('Client is connected to a chat server!\n')


    # call the function to send message to server
    sndThread = threading.Thread(target = send_to_server, args = (clientSocket,))
    # call the function to receive message server
    rcvThread = threading.Thread(target = recv_from_server, args = (clientconnection,))

    sndThread.start()
    rcvThread.start()


# This is where the program starts
if __name__ == '__main__':
    main()
