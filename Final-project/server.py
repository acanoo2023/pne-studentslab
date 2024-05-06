import http.server
import http.client
import json
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

def get_json(endpoint, params):
    SERVER = "rest.ensembl.org"

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
        if path.startswith("/listSpecies"):
            data = get_json("/info/species", "?content-type=application/json")
            print(arguments)

            my_list = []
            for i in range(0, len(data["species"])):
                my_list.append(data["species"][i]["display_name"])

            print(my_list)

            content = read_html_file("species.html").render(context={"list_species": my_list, "species_length": len(data["species"]), "user_limit": int(arguments["user_limit_1"][0])})
        if path.startswith("/karyotype"):  #ME HE QUEDADO AQUÍ, TENGO QUE SACAR EL CONTENIDO DE LOS CROMOSMAS DESDE ENSEMBL COMO ANTES CON LAS ESPECIES Y LUEGO UN LOOP EN EL HTML







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

