import socket

 

localIP     = "127.0.0.1"

localPort   = 9090

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client: "

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientMsg2 = "Message from Client:{}".format(message.decode())
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg2)
    print(clientIP)

   

    # Sending a reply to client

    bytesToSendDec = msgFromServer + message.decode() 

    UDPServerSocket.sendto(bytesToSendDec.encode(), address)

