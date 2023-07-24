import socket

client_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 5555

client_object.connect((ip_address, port))

data_receive = client_object.recv(1024)

if data_receive:
    print("CLIENT CONNECTED TO SERVER")
    print(data_receive.decode("utf-8"))
    
    
    while data_receive:
        client_input = input().encode("utf-8")
        
        client_object.send(client_input)
        
        data_receive = client_object.recv(1024)
        if data_receive:
            print("{}: {}" .format("SERVER", data_receive.decode("utf-8")))