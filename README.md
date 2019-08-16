# Full-Duplex-Chat
The server will listen for a TCP connection from the client. Once a connection has been established between the server and client, you may begin sending messages to each other. This is a full duplex chat, meaning the client and server can send messages at the same time as both hosts will have sending and receiving threads (multithreaded).

Steps to run:

1. First run the server: python3 chatServerDuplex.py

2. After the server is running, run the client in a seperate terminal: python3 chatClientDuplex.py
