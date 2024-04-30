import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j


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
            print(arguments)
            #length = arguments[0]
            #limit = arguments[1]
            content = Path("species.html").read_text()
            #.render(context={"species_length": length, "user_limit": limit})




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