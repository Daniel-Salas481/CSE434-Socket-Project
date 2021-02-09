from socket import *
serverPort = 5050
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("", serverPort))
print("[RUNNING]")

while True:
    register, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode().upper()
    #FAILURE if the contact name exist
    print("responded")
    sucess = "SUCCESS"
    serverSocket.sendto(sucess.encode(), clientAddress)

