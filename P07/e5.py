from Seq1 import Seq
import http.client
import json
import termcolor

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

for gene in genes:

    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/"
    IDENTIFIER = genes[gene]
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + IDENTIFIER + PARAMS

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", ENDPOINT + IDENTIFIER + PARAMS)
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
    data_1_json = json.loads(data1)
    #If print "print(data_1_json)" all the information can be seeing


    termcolor.cprint("Gene", 'green', end="")
    print(": " + gene)
    termcolor.cprint("Description", 'green', end="")
    description = data_1_json["desc"]
    print(": " + description)

    s1 = Seq(data_1_json["seq"])

    termcolor.cprint("Total length: " + str(s1.len()))

    bases = ["A", "C", "G", "T"]

    for base in bases:
        termcolor.cprint(base, 'blue', end="")
        amount = s1.count_base(base)
        percentage = (amount * 100) / s1.len()
        print(": " + str(amount) + " (" + str(round(percentage, 1)) + "%)")

    termcolor.cprint("Most frequent Base: " + s1.most_frequent())






