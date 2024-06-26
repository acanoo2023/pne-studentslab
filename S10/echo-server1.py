import socket
from termcolor import colored

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")


while True:
    # -- Waits for a client to connect
    print("\nWaiting for Clients to connect...")

    try:
        (cs, client_ip_port) = ls.accept() #This method returns a tupple (client socket, and address)

    # -- Server stopped manually by the user:
    except KeyboardInterrupt:
        print("\nServer stopped by the user")

        # -- Close the listening socket so that it doesn't receive more entries from users
        ls.close()

        # -- Exit!
        exit()

    # -- If the user doesn't close the program --> Execute this part
    else:

        print("\tA Client has connected to the server!!")


        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)   #This function is just for reading

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()   #This function translate to "string language"

        # -- Print the received message
        print("\tMessage received: ", colored(msg, "yellow"))

        # -- Send a response message to the client
        response = "ECHO: " + msg + "\n" #Message that we (server) send back to the server after he writes us

        # -- The message has to be encoded into bytes (transformed into computer language)
        cs.send(response.encode())

        # -- Close the data socket (from the user)
        cs.close()

