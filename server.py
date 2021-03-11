from multiprocessing import Process, current_process, Queue

from socket import *


serverPort = 5050
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(("", serverPort))
print("[RUNNING]")



class ContactList:
    def __init__(self, _name):  #join asu daniel 
        self.name = _name       #does "asu" exist? 
        self.contact = []       # does daniel exist in "asu"
    def addContact(self, contact):
        self.contact.append(contact)

class Contactinfo:
    def __init__(self, name, ipAdd, portNum):
        self.name = name
        self.ipAdd = ipAdd
        self.portNum = portNum


p = [] 
contactName = []
messageHolder = ""
#holding the name and contact to see if it equals
nameHolder = ""
contactHolder = "" 

#def se_imcomplete():

 #   imComCon, clientAddress = serverSocket.recvfrom(2048)
  #  imNamCon, clientAddress = serverSocket.recvfrom(2048)


def se_messageStore(nam , com, mes):

    
    #imComCon, clientAddress = serverSocket.recvfrom(2048)
    #imNamCon, clientAddress = serverSocket.recvfrom(2048)

    #imNam = imNamCon.decode()
    #imCom = imComCon.decode()

    username = nam
    contact = com 
    message = mes
    
    print(f"___________________")
    print(f"{username}: {message} ")
    print(f"___________________")

    serverSocket.sendto("1".encode(), clientAddress)
    serverSocket.sendto(contact.encode(), clientAddress)
    serverSocket.sendto(username.encode(), clientAddress)
    serverSocket.sendto(message.encode(), clientAddress)

    

#what is going to do multiple work
def se_multiProcess():
    if __name__ == "__main__":
        queue = Queue()
    
    imStore, clientAddress = serverSocket.recvfrom(2048)

    global messageHolder

    messageHolder = imStore.decode()

    multiCom, clientAddress = serverSocket.recvfrom(2048)
    multiNam, clientAddress = serverSocket.recvfrom(2048)
  

    Nam = multiNam.decode()
    Com = multiCom.decode()


    processes = [Process(target=se_messageStore, args=(Nam, Com, messageHolder))]

    for p in processes:
        p.start() #we start here
        
    for p in processes:
        p.join() #use the join in order to stop execution of current program

         



def se_imstart():
    imContact, clientAddress = serverSocket.recvfrom(2048)
    imName, clientAddress = serverSocket.recvfrom(2048)
    
    counter = 0
    decodeCon = imContact.decode()
    decodeNam = imName.decode()
    

    contactValid = False
    nameValid = False
    contactString = str(len(contactName))#list of name in

    for cl in contactName:
        if cl.name == decodeCon:
            contactValid = True
            print(f"Found contact list: {cl.name}")
        else:
            print("Not found")
        
    
    if contactValid == True:
        for i,j in enumerate(contactName):
            
            for u in j.contact:
                
                print(f"Loopin in {u.name}")
                
                if u.name == decodeNam:
                    nameValid = True

                    print(f"contact name: {u.name}")
                    print(f"IP Address: {u.ipAdd}")
                    print(f"portNumber: {u.portNum}")
                    print(f"Moving it to top of the  list....")
                    
                    # moving up the selected contact list to the start index
                    j.contact.insert(0, j.contact.pop())
                else:
                    print("Not this one..")
               
            for h in j.contact:#here
                print(f" setting up {h.name}")
                contactString += h.name + " " + h.ipAdd + " " + str(h.portNum) + " "

    if contactValid == True and nameValid == True:
        print(f"sending the contact list with {decodeNam} ")

        global nameHolder
        nameHolder = decodeNam

        global contactHolder
        contactHolder = decodeCon

        #contactString = str(len(contactName)) + " "
       # for cl in contactName: #Need to only show the list with name you input. not the others
           # contactString += cl.name + " " + str(len(cl.contact)) + " "
        
        serverSocket.sendto(contactString.encode(), clientAddress)

        serverSocket.sendto("0".encode(), clientAddress)        

    else: 
        fValid = "Failure: 0"
        serverSocket.sendto(fValid.encode(), clientAddress)


    #serverSocket.sendto(fValid.encode(), clientAddress)
    
    
def se_exit():
    exName, clientAddress = serverSocket.recvfrom(2048)

    decodeExit = exName.decode()

    nonContact = False
    inContact = False

    for i,j in enumerate(p):
        if j.name == decodeExit:
            print(f"found {j.name} outside of contact list...")
            nonContact = True
            p.remove(j)
    
    for i,j in enumerate(contactName):
        for u in j.contact:
            if u.name == decodeExit:
                print(f"found {u.name} in a Contact list. Removing...")
                inContact = True
                j.contact.remove(u)
    
    if nonContact == True or inContact == True:
        isValid = "SUCCESS"
        print("Removed success")
        serverSocket.sendto(isValid.encode(), clientAddress)
    
    if nonContact == False and inContact == False:
        isValid = "FAILURE"
        print("Removed Failed...")
        serverSocket.sendto(isValid.encode(), clientAddress)




def se_save():
    saveName, clientAddress = serverSocket.recvfrom(2048)

    decodeSave = saveName.decode()

    outfile = open(decodeSave+".txt", 'w')

    # A line containing the number of n of active users (or contacts)
    TextFileData = str(len(p)) + "\n"

    # For each of the n contacts
    for contact in p:
        # A line containing the contact-name, its ip address, and port number
        TextFileData += contact.name + " " + contact.ipAdd + " " + contact.portNum + "\n"

    # A line containing the number of l of contact lists
    TextFileData += str(len(contactName)) + "\n"

    # For each fo the l contact lists
    for cl in contactName:
        # A line containig the contact-list-name followed by the number k of contacts in the list
        TextFileData += cl.name + " " + str(len(cl.contact)) + "\n"

        # For each of the k contacts 
        for contact in cl.contact:
            # A line containing the contact-name, it's ip address and its port number 
            TextFileData += contact.name + " " + contact.ipAdd + " " + str(contact.portNum) + "\n"
   
    # Debug Print
    #print(TextFileData)
    if not decodeSave:
        print("Failed to create")
        isValid = "FAILURE"
        serverSocket.sendto(isValid.encode(), clientAddress)
        outfile.close()
    else:
        print("File Created")
        isValid = "SUCCESS"
        outfile.write(TextFileData)
        serverSocket.sendto(isValid.encode(), clientAddress)
        outfile.close()
    

    

def se_join():
    conList, clientAddress = serverSocket.recvfrom(2048)
    nameList, clientAddress = serverSocket.recvfrom(2048)


    decodeC = conList.decode()
    decodeN = nameList.decode()

    nameValid = False
    contactValid = False
    regValid = False
    inList = False
    for i,j in enumerate(contactName):
        if j.name == decodeC:
            contactValid = True
            print("Contact: " + j.name + " found")
            for u in j.contact:
                if u.name == decodeN:
                    inList = True
                    print("already exist")
            
            if inList == False:
                for y in p:
                    if y.name == decodeN:
                        print("Name: " + y.name + " " +
                        "Ip Address: " + y.ipAdd + " " +
                        "Port Number: " + str(y.portNum) + "\n")
                        theInfo = Contactinfo(y.name, y.ipAdd, y.portNum)
                        contactName[i].addContact(theInfo)
                        nameValid = True
            #ContactLists[0].addContact(theInfo)
    if nameValid == True and contactValid == True:
        print("Added to contact succesfully")
        isValid = "SUCCESS"
        serverSocket.sendto(isValid.encode(), clientAddress)
    else:
        print("An error has occurred")
        isValid = "FAILURE"
        serverSocket.sendto(isValid.encode(), clientAddress)
  



    
    #decodeConList = conList.decode()
    #decodeNameList = nameList.decode()


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
        success = "SUCCESS"
        serverSocket.sendto(success.encode(), clientAddress)
        conValid = False
    #perhaps???/
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
        success = "SUCCESS"
        serverSocket.sendto(success.encode(), clientAddress)




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
        print(f'active users: {len(p)}')
        print(f'Values are stored')
        success = "SUCCESS"
        serverSocket.sendto(success.encode(), clientAddress)
    



    for obj in p:
        if obj.name == decodeName:
            success = "FAILURE"
            serverSocket.sendto(success.encode(), clientAddress)
            regValid = False
    
    if(regValid == True):   
        p.append(Contactinfo(decodeName, decodeIP,decodePort))
        print("responding...")
        print(f'contact-name: {decodeName}')
        print(f'IP-address: {decodeIP}')
        print(f'port: {decodePort}')
        print(f'active users: {len(p)}')
        print(f'Values are stored')
        success = "SUCCESS"
        serverSocket.sendto(success.encode(), clientAddress)




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
    elif(command == "4"):
        se_save()
    elif(command == "5"):
        se_exit()
    elif(command == "6"):
        se_imstart()
    elif(command == "8"):
        se_multiProcess()
    else:
        print("command error")
   
    
    
    
    

