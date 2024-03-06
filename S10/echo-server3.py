import socket
import termcolor

PORT = 8081
IP = "212.128.255.90"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

client_counter = 1
clients_list = []

while True:
    print("\nWaiting for Clients to connect...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:     # -- Server stopped manually by the user:
        print("\nServer stopped by the user")
        ls.close()
        exit()

    else:    # -- If the user doesn't close the program --> Execute this part
        print(f"\tCONNECTION {client_counter}. Client IP,PORT: {client_ip_port}")
        clients_list.append(client_ip_port)

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        print(f"\tMessage received: " + termcolor.colored(msg, "green"))

        response = "ECHO: " + msg + "\n"

        cs.send(response.encode())

        cs.close()

        if client_counter % 5 == 0:
            print("\nThe following clients have connected to the server: ")
            for i in range(0,5):
                print(f"Client {i}: {clients_list[i-1]}")

            clients_list = []

        client_counter += 1


