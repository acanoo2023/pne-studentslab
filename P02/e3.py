from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#           (To run this exercise, first you must run the server created in S08)


# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")  #Here I put the message that I want to send to the server
print(f"Response: {response}")

