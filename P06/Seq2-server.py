import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

my_sequences = ["ACACGTTACGACTACGCATCGA", "CAGTAGACGTTTGAAGTAGCCGA", "GTTACTCATCAACGACTACGACT", "TCAGTCTTCAACGTACACACGTG", "TTACGCGCATCGCATACGCTA"]

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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
        elif path.startswith("/ping"):
            content = Path("./html/ping.html").read_text()
            print(arguments)   #I print the arguments to see what I get on the arguments variable
                               #Since we just have 1 input, our dictionary will have just 1 key-value
        elif path.startswith("/get"):
            number_choice = arguments["n"][0]
            seq_chosen = my_sequences[int(number_choice)]
            content = read_html_file("get.html").render(context={"user_choice": number_choice, "sequence": seq_chosen})
            print(arguments)
        elif path.startswith("/gene"):
            gene_choice = arguments["name"][0]
            print(gene_choice)
            gene_chosen = Path("../P02/sequences/" + gene_choice + ".txt")
            print(gene_chosen)
            content = read_html_file("gene.html").render(context={"user_choice": gene_choice, "gene": gene_chosen})
            print(arguments)

        else:
            content = Path("./html/error.html").read_text()
            self.send_response(404)  # -- Status line: NOT FOUND


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
