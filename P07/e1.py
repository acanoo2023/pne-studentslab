import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()



print()
print("Server: " + SERVER)
print("URL: " + URL)
# -- Print the status line
print(f"Response received!: {response.status} {response.reason}\n")

# -- Read the response's body
data1 = response.read().decode("utf-8")
data_1_jason = json.loads(data1)

if data_1_jason["ping"] == 1:
    print("PING OK! The database is running!")
else:
    print("The database is not running")