from socket import *


serverPort = 5050
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("", serverPort))
print("[RUNNING]")



class ContactList:
    def __init__(self, _name):
        self.name = _name
        self.contact = []
    def addContact(self, contact):
        self.contact.append(contact)

class Contactinfo:
    def __init__(self, name, ipAdd, portNum):
        self.name = name
        self.ipAdd = ipAdd
        self.portNum = portNum


p = []
contactName = []

def se_join():
    conList, clientAddress = serverSocket.recvfrom(2048)
    nameList, clientAddress = serverSocket.recvfrom(2048)

    for obj in contactName:
        if obj.name == nameList:
    
    decodeConList = conList.decode()
    decodeNameList = nameList.decode()


#most likely will work on this more after I start working on the add function
def se_query():
    if not ContactList:
        print(f'No contact is found')
        noContactMsg = "No contact has been created"
        noContact = str(0)
        serverSocket.sendto(noContact.encode(), clientAddress)
        serverSocket.sendto(noContactMsg.encode(), clientAddress)
    
    else:
        contactString = str(len(contactName)) + " "
        for cl in contactName:
            contactString += cl.name + " " + str(len(cl.contact)) + " "
            for contact in cl.contact:
                contactString += contact.name + " " + contact.ipAdd + " " + str(contact.portNum) + " "
        contactArray = contactString.split()

        NumberOfContactLists = int(contactArray[0])
        TotalPos = 1
        for i in range(NumberOfContactLists):
            MyContactListName = contactArray[TotalPos]
            TotalPos += 1
            MyContactListSize = int(contactArray[TotalPos])
            TotalPos += 1
            for x in range(MyContactListSize):
                MyContactName = contactArray[TotalPos]
                TotalPos += 1
                MyContactIp = contactArray[TotalPos]
                TotalPos += 1
                MyContactPort = contactArray[TotalPos]
                TotalPos += 1
        contactArray = contactString.split()

        NumberOfContactLists = int(contactArray[0])
        TotalPos = 1
        for i in range(NumberOfContactLists):
            print("Contact List Name: " + contactArray[TotalPos] + " ")
            TotalPos += 1
            MyContactListSize = int(contactArray[TotalPos])
            print("Total Number of contacts in list: " + str(MyContactListSize)+ "\n")
            TotalPos += 1
            for x in range(MyContactListSize):
                print("Name: " + contactArray[TotalPos]+ " ")
                TotalPos += 1
                print("Ip: " +contactArray[TotalPos]+ " ")
                TotalPos += 1
                print("Port: " + contactArray[TotalPos]+ " ")
                TotalPos += 1
                print("\n")        
        #numOfContact = str(len(contactName))
       # str1 = " "
       # stringContact = str1.join(ContactList)
        serverSocket.sendto(contactString.encode(), clientAddress)
        
        
        
def se_create():
    ContactListin, clientAddress = serverSocket.recvfrom(2048)
    

    #decode the values
    decodeContact = ContactListin.decode()
    
    conValid = True

    if not contactName:
        theContact = ContactList(decodeContact)
        contactName.append(theContact)
        print("responding...")
        print(f'contact: {decodeContact}')
        print(f'Contact list is made')
        sucess = "SUCCESS"
        serverSocket.sendto(sucess.encode(), clientAddress)
        conValid = False
    
    if decodeContact in contactName:
        response = "FAILURE"
        serverSocket.sendto(response.encode(), clientAddress)
        conValid = False
    
    if(conValid == True):   
        theContact = ContactList(decodeContact)
        contactName.append(theContact)
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
    elif(command == "2"):
        se_query()
    elif(command == "3"):
        se_join()
    else:
        print("command error")
   
    
    
    
    

