from socket import *
from consolemenu import *
from consolemenu.items import *
import re

serverName = '127.0.0.1'

serverPort = 5050
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Create the menu
menu = ConsoleMenu("IM messaging app", "Milestone Demo (CSE-434)", show_exit_option=False)






# Create some items
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
      #register = input("..")
    exit()
    
   
def op_create():

    ContactListin = input("create ")

    

IMregister = FunctionItem("register", op_register)

IMcreate = FunctionItem("create", op_create)

IMquery = CommandItem("query-lists",  "echo hello")

IMjoin = FunctionItem("join", input, ["Enter an input"])

IMsave = FunctionItem("save", input, ["Enter an input"])

IMexit = FunctionItem("exit", input, ["Enter an input"])

# Once we're done creating them, we just add the items to the menu
menu.append_item(IMregister)
menu.append_item(IMcreate)
menu.append_item(IMquery)
menu.append_item(IMjoin)
menu.append_item(IMsave)
menu.append_item(IMexit)


# Finally, we call show to show the menu and allow the user to interact
menu.show()



#message = input('Input lowercase Sentence:')
#clientSocket.sendto(message.encode(),(serverName, serverPort))
#modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#print(modifiedMessage.decode())
#clientSocket.close()