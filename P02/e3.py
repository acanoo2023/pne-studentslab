from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.92" # your IP address
PORT = 5362

# -- Create a client object
c = Client(IP, PORT)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")  #Here I put the message that I want to send to the server
print(f"Response: {response}")

