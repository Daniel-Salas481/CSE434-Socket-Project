from socket import *
from consolemenu import *
from consolemenu.items import *
import time 
import re

serverName = '127.0.0.1'

serverPort = 5050
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Create the menu
menu = ConsoleMenu("IM messaging app", "Final Project (CSE-434)", show_exit_option=False)


# Create some items


backed = False
    

def op_imstart():
    imStartContact, imStartName = input("im-start ").rsplit(None, 1)

    clientSocket.sendto("6".encode(), (serverName, serverPort))
    clientSocket.sendto(imStartContact.encode(),(serverName, serverPort))
    clientSocket.sendto(imStartName.encode(),(serverName, serverPort))

    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())


    cmd_encoded, clientAddress = clientSocket.recvfrom(2048)
    command = cmd_encoded.decode()

    i = True
    while True:
        if(command == "0"): #Now sending the message
            imMessage = "Type Your Message:" 
            inputStr = input(imMessage)  


            #calling and sending message to server
            clientSocket.sendto("8".encode(), (serverName, serverPort))
            clientSocket.sendto(inputStr.encode(),(serverName, serverPort)) 
            

            #im-complete <contact-list-name> <contact-name>
            clientSocket.sendto(imStartContact.encode(), (serverName, serverPort))
            clientSocket.sendto(imStartName.encode(), (serverName, serverPort))

            #Success or Failure indicated
            #May have to exit somehow
        cmd_code, serverAddress = clientSocket.recvfrom(2048)
        command1 = cmd_code.decode()
        if(command1 == "1"):
            #recieved the message back from the server and now it outputs to everyone


            #listen to the socket in the child process. 
            contactCode, clientAddress = clientSocket.recvfrom(2048)
            usernameCode, clientAddress = clientSocket.recvfrom(2048)
            messageCode, clientAddress = clientSocket.recvfrom(2048)

            contact = contactCode.decode()
            username = usernameCode.decode()
            message = messageCode.decode()

            print(f"{username} said: [{message}]")


    

def op_exit():
    exitIn = input("exit ")

    clientSocket.sendto("5".encode(), (serverName, serverPort))
    clientSocket.sendto(exitIn.encode(), (serverName, serverPort))

    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())
    exit()
    



def op_save():
    saveIn = input("save ")

    
    clientSocket.sendto("4".encode(), (serverName, serverPort))
    clientSocket.sendto(saveIn.encode(), (serverName, serverPort))
    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())
    exit()

    

def op_join():
    joinConList, joinConName = input("join ").rsplit(None, 1)

    clientSocket.sendto("3".encode(), (serverName, serverPort))
    clientSocket.sendto(joinConList.encode(),(serverName, serverPort))
    clientSocket.sendto(joinConName.encode(),(serverName, serverPort))

    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())
    exit()
 

def op_register():
    #register <contact-name> <IP-address> <port>.
    validIP = False
    
    # Regex expression for validating IPv4
    regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])\\.){3}"\
            "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])"

    p = re.compile(regex)

    nameReg, ipReg, portReg = input("register ").rsplit(None, 2)

    
    if nameReg.isalpha() and re.search(p, ipReg) and portReg.isdigit():
     clientSocket.sendto("0".encode(),(serverName, serverPort)) #letting the server know it is a register function
     clientSocket.sendto(nameReg.encode(),(serverName, serverPort))
     clientSocket.sendto(ipReg.encode(),(serverName, serverPort))
     clientSocket.sendto(portReg.encode(),(serverName, serverPort))
     messageCom, serverAddress = clientSocket.recvfrom(2048)
     print(messageCom.decode())
     exit()
     
    else:
     print('Invalid input. Please try again.')
     exit()
     
    
   
def op_create():

    ContactListin = input("create ")
    
    clientSocket.sendto("1".encode(), (serverName, serverPort))
    clientSocket.sendto(ContactListin.encode(), (serverName, serverPort))
    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())
    exit()
    

def op_query():
    clientSocket.sendto("2".encode(), (serverName, serverPort))
    messageCom, serverAddress = clientSocket.recvfrom(2048)
    print(messageCom.decode())
    exit()
    



    

IMregister = FunctionItem("register", op_register)

IMcreate = FunctionItem("create", op_create)

IMquery = FunctionItem("query-lists",  op_query)

IMjoin = FunctionItem("join", op_join)

IMsave = FunctionItem("save", op_save)

IMstart = FunctionItem("im-start", op_imstart)

IMexit = FunctionItem("exit", op_exit)



# Once we're done creating them, we just add the items to the menu
menu.append_item(IMregister)
menu.append_item(IMcreate)
menu.append_item(IMquery)
menu.append_item(IMjoin)
menu.append_item(IMsave)
menu.append_item(IMstart)
menu.append_item(IMexit)


# Finally, we call show to show the menu and allow the user to interact
menu.show()
