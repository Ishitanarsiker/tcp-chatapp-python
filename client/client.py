import socket
import sys
import os
from utility import send_file, recv_file, recv_listing

client_files_path = "./"

try:
    # If the number of args is not 3 or 4 the program will terminate
    if len(sys.argv)== 4 or len(sys.argv)== 5: 
    
        host = sys.argv[1]
        port = int(sys.argv[2])
        
        command = sys.argv[3:]
        user_input = ' '.join(command)
        
    else:
        print("Invalid number of arguments")
        exit(1)
        
    # Create the socket with which we will connect to the server    
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    cli_sock.connect((host, port))
     
    print("Client Connected to server.\n" )
    
    if (command[0] == "list"):
        cli_sock.sendall(str.encode(user_input))
        
        files = recv_listing(cli_sock)
        
        print ("List of files received from server:")
       
        for index, file in enumerate(files):
            print(str(index + 1) + ') ' + file)
    
    else:
        
        filePath = os.path.join(client_files_path, command[1])
        
        if (command[0] == "put"):
            cli_sock.sendall(str.encode(user_input))
            send_file(filePath,cli_sock)
        
        elif (command[0] == "get"):
            cli_sock.sendall(str.encode(user_input))
            recv_file(filePath,cli_sock)
        
except Exception as e:
    print(e)
     # Exit with a non-zero value, to indicate an error condition
    exit(1)
finally:
    cli_sock.close()

    # Exit with a zero value, to indicate success
exit(0)