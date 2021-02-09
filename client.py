from socket import *
from consolemenu import *
from consolemenu.items import *

serverName = '127.0.0.1'

serverPort = 5050
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Create the menu
menu = ConsoleMenu("IM messaging app", "Milestone Demo (CSE-434)", show_exit_option=False)

# Create some items
def op_register():
    #register <contact-name> <IP-address> <port>.
    register = input("register ")
    clientSocket.sendto(register.encode(),(serverName, serverPort))
    messageCom, serverAddress = clientSocket.recvfrom(2048)

    print(messageCom.decode())
    register = input("..")
    exit()

    

IMregister = FunctionItem("register", op_register)

IMcreate = FunctionItem("create", input, ["Enter an input"])

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
