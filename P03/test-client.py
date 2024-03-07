from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

print("-----| Practice 3, Exercise 7 |------")

c = Client(IP, PORT)

print("Testing PING:")
print(c.talk("PING"))

print("Testing GET:")
for i in range(0,5):
    result = "GET " + str(i) + ": " + c.talk("GET " + str(i))
    clean = result.rstrip("\n")
    print(clean)
print("\n")

seq = c.talk("GET 0")

print("Testing INFO:")
print(c.talk("INFO " + seq))

print("Testing COMP:")
print(c.talk("COMP " + seq))

print("Testing REV:")
print(c.talk("REV " + seq))

filename_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for i in filename_list:
    print("GENE " + str(i))
    print(c.talk("GENE "+ str(i)))
