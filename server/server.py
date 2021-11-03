import socket
import sys
import os
from utility import send_file, recv_file, send_listing, recv_listing


srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   srv_sock.bind(("0.0.0.0", int(sys.argv[1])))
   srv_sock.listen(5)
   print ("Server is up and running at port " + sys.argv[1])
   
except Exception as e:
   print(e)
   # Exit with a non-zero value, to indicate an error condition
   exit(1)

while True:
    try:
        print("Finding a new client... ")
        
        cli_sock, cli_addr = srv_sock.accept()
        
        print("New client connected at " + str(cli_addr))

        commandList = cli_sock.recv(1024)
        command = commandList.decode().split(" ", 1)
        
        if (command[0] == "list"):
            send_listing(cli_sock, "./")
        else:
            fileName = os.path.join("./", command[1])
        
        if (command[0] == "put"):
            recv_file(fileName,cli_sock)
        elif (command[0] == "get"):
            send_file(fileName,cli_sock)

    finally:
        cli_sock.close()
    exit (0)