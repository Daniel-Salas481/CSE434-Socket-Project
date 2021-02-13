from socket import *


serverPort = 5050
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("", serverPort))
print("[RUNNING]")


class Contactinfo:
    def __init__(self, name, ipAdd, portNum):
        self.name = name
        self.ipAdd = ipAdd
        self.portNum = portNum
       

#class ContactList:
 #   def __init__(self, conName):
  #      self.conName =  conName


p = []
contactName = []

def se_create():
    ContactListin, clientAddress = serverSocket.recvfrom(2048)
    

    #decode the values
    decodeContact = ContactListin.decode()
    
    conValid = True

    if not contactName:
        contactName.append(decodeContact)
        print("responding...")
        print(f'contact: {decodeContact}')
        print(f'Contact list is made')
        sucess = "SUCCESS"
        serverSocket.sendto(sucess.encode(), clientAddress)
    
    if decodeContact in contactName:
        response = "FAILURE"
        serverSocket.sendto(response.encode(), clientAddress)
        conValid = False
    
    if(conValid == True):   
        contactName.append(decodeContact)
        print("responding...")
        print(f'contact: {decodeContact}')
        print(f'Contact list is made')
        sucess = "SUCCESS"
        serverSocket.sendto(sucess.encode(), clientAddress)




def se_register():
    nameReg, clientAddress = serverSocket.recvfrom(2048)
    ipReg, clientAddress = serverSocket.recvfrom(2048)
    portReg, clientAddress = serverSocket.recvfrom(2048)
    

    #decoding the values
    decodeName = nameReg.decode()
    decodeIP = ipReg.decode()
    decodePort = portReg.decode()
    regValid = True #true by default


    if not p:
        p.append(Contactinfo(decodeName, decodeIP,decodePort))
        print("responding...")
        print(f'contact-name: {decodeName}')
        print(f'IP-addres: {decodeIP}')
        print(f'port: {decodePort}')
        print(f'Values are stored')
        sucess = "SUCCESS"
        serverSocket.sendto(sucess.encode(), clientAddress)
    



    for obj in p:
        if obj.name == decodeName:
            sucess = "FAILURE"
            serverSocket.sendto(sucess.encode(), clientAddress)
            regValid = False
    
    if(regValid == True):   
        p.append(Contactinfo(decodeName, decodeIP,decodePort))
        print("responding...")
        print(f'contact-name: {decodeName}')
        print(f'IP-addres: {decodeIP}')
        print(f'port: {decodePort}')
        print(f'Values are stored')
        sucess = "SUCCESS"
        serverSocket.sendto(sucess.encode(), clientAddress)




while True:

    cmd_encoded, clientAddress = serverSocket.recvfrom(2048)

    command = cmd_encoded.decode()

    if(command == "0"):
        se_register()
    elif(command == "1"):
        se_create()
    else:
        print("command error")
   
    
    
    
    

