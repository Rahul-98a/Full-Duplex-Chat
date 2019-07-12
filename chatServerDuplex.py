# Import socket module
from socket import *
import sys # In order to terminate the program
import threading

FLAG = False  # this is a flag variable for checking quit

# function for receiving message from server
def recv_from_client(clsock):
    while True:
        data = clsock.recv(1024).decode()
        if data == 'q':
            print('Closing connection')
            sys.exit()
        if data != False:
           print('Message Received: ', data)

# function for receiving message from client
def send_to_client(conn):
    global FLAG
    while True:
        try:
            send_msg = input('Type Message: ')
		     # the server can provide 'q' as an input if it wish to quit
            if send_msg == 'q':
                conn.send('q'.encode())
                print('Closing connection')
                conn.close()
                FLAG = True
                conn.send(send_msg.encode())
            conn.send(send_msg.encode())
        except:
            conn.close()






# this is main function
def main():
	global FLAG

	# TODO (1) - define HOST name, this would be an IP address or 'localhost' (1 line)
	HOST = 'localhost'
	# TODO (2) - define PORT number (1 line) (Google, what should be a valid port number)
	# make sure the ports are not used for any other application
	serverPort = 65535
	serverPort2 = 65534

	# Create a TCP server socket
	#(AF_INET is used for IPv4 protocols)
	#(SOCK_STREAM is used for TCP)
	# TODO (3) - CREATE a socket for IPv4 TCP connection (1 line)
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket2 = socket(AF_INET, SOCK_STREAM)

	# Bind the socket to server address and server port
	# TODO (4) - bind the socket for HOST and serverPort (1 line)
	serverSocket.bind(('', serverPort))

	# Listen to at most 1 connection at a time
	# TODO (5) - listen and wait for request from client (1 line)

	serverSocket.listen(1)

	# Server should be up and running and listening to the incoming connections
	print('The chat server is ready to connect to a chat client')
	# TODO (6) - accept any connection request from a client (1 line)
	connectionSocket, addr = serverSocket.accept()

	print('Server is connected with a chat client\n')


	# request connection to client, and get client's receiving socket
	serverSocket2.connect((HOST, serverPort2))


	# This is the loop for chating, the connection is already made with the
	# client now the server and client will be able to chat with each other
    # call the receive function
	recvThread = threading.Thread(target = recv_from_client, args = (connectionSocket,))
	sndThread = threading.Thread(target = send_to_client, args = (serverSocket2,))


		
	recvThread.start()
	sndThread.start()
	#Terminate the program after sending the corresponding data
	sys.exit()


# This is where the program starts
if __name__ == '__main__':
	main()
