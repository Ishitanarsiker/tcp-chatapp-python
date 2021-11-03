import socket
import os
import json

def send_listing(sock, files_path):

    files = str(os.listdir("./"))
    sock.sendall(files.encode('utf-8'))
        
    print ("List of directory sent to Client")
    
def recv_listing(sock): 
    data = sock.recv(1024).decode('utf-8')
    print(data)
    files = data.strip('][').replace('"', '').split(',') # converting string representation of list to python list
    return files
  
  
def send_file(filePath,sock):

    print("Sending file: " + filePath)
    
    if os.path.isfile(filePath): 
        with open(filePath, 'rb') as f:
                for data in f:
                    sock.sendall(data)
    else:
        raise IOError("Invalid file name")
  

def recv_file(filePath, sock):
    print("Saving file at: " + filePath)
    
    if os.path.isfile(filePath): 
        print("Overwritting file")
        
    with open(filePath, 'wb') as f:
        while True:
            data = sock.recv(1024)
            if data:
                f.write(data)
            else:
                break
                
    print ("File received successfully")