import http.server
import http.client
import json
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq


def get_json(endpoint):
    SERVER = "rest.ensembl.org"
    params = "?content-type=application/json"
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", endpoint + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    response = conn.getresponse()
    data1 = response.read().decode("utf-8")
    data_1_json = json.loads(data1)

    return data_1_json


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Parse URL path and query arguments
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        content = ""

        if path == "/":
            content = Path("./html/index.html").read_text()
            self.send_response(200)  # -- Status line: OK!

        elif path.startswith("/listSpecies"):
            try:
                if (arguments["limit"][0]).isdigit() and int(arguments["limit"][0]) >= 0:
                    data = get_json("/info/species")
                    print(arguments)

                    my_list = []
                    for i in range(0, len(data["species"])):
                        my_list.append(data["species"][i]["display_name"])
                    print(my_list)
                    content = read_html_file("species.html").render(context={"list_species": my_list, "species_length": len(data["species"]), "user_limit": int(arguments["limit"][0])})
                else:
                    content = Path("./html/error.html").read_text()
            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/karyotype"):
            print(arguments)
            try:
                data = get_json("info/assembly/" + arguments["specie"][0].replace(" ", "%20"))

                karyotype_info = []
                for i in data["karyotype"]:
                    karyotype_info.append(i)
                print(karyotype_info)
                content = read_html_file("karyotype.html").render(context={"list_karyotype": karyotype_info})
            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/chromosomeLength"):
            print(arguments)
            try:
                data = get_json("info/assembly/" + arguments["specie"][0])
                if arguments["user_chromosome"][0] in data["karyotype"]:
                    length = ""
                    for info_dict in data["top_level_region"]:
                        if arguments["user_chromosome"][0] == info_dict["name"]:
                            length = info_dict["length"]

                    content = read_html_file("chromosome.html").render(context={"chromosome_length": length})
                else:
                    content = Path("./html/error.html").read_text()
            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/geneSeq"):
            print(arguments)
            try:
                data1 = get_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                id = data1["id"]
                print(id)
                data2 = get_json("/sequence/id/" + id)
                result_gene = data2["seq"]
                print(result_gene)

                content = read_html_file("seq.html").render(context={"user_gene": arguments["gene"][0], "gene_seq": result_gene})
            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/geneInfo"):
            print(arguments)
            try:
                data1 = get_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                id = data1["id"]
                data2 = get_json("/sequence/id/" + id)
                result_gene = data2["seq"]

                data = get_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])

                content = read_html_file("info.html").render(context={"user_gene": arguments["gene"][0], "start": data["start"], "end": data["end"], "id": id, "length": len(result_gene)})

            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/geneCalc"):
            print(arguments)
            try:
                data1 = get_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                id = data1["id"]
                data2 = get_json("/sequence/id/" + id)
                result_gene = data2["seq"]

                s1 = Seq(result_gene)

                termcolor.cprint("Total length: " + str(s1.len()))

                my_list = []
                bases = ["A", "C", "G", "T"]
                for base in bases:
                    amount = s1.count_base(base)
                    percentage = (amount * 100) / s1.len()
                    my_list.append(base + ": " + str(amount) + " (" + str(round(percentage, 1)) + "%)")
                print(my_list)
                content = read_html_file("calc.html").render(context={"user_gene": arguments["gene"][0], "list_percentages": my_list, "length": s1.len()})

            except KeyError:
                content = Path("./html/error.html").read_text()

        elif path.startswith("/geneList"):
            print(arguments)


            content =read_html_file("list.html").render(context={})
























        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(content))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

