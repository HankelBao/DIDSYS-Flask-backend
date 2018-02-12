from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib import parse

class DirectAPIApp:
    def __init__(self, port, directApiRegister):
        self.port = port
        self.Handler.DirectAPIRegister = directApiRegister

    def run(self):
        print("Start Running App...")

        server = HTTPServer(('', self.port), self.Handler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("C-C detected, killing server...")
            pass
        finally:
            server.server_close()
        print("Bye")

    class Handler(BaseHTTPRequestHandler):
        DirectAPIRegister = None 

        def do_GET(self):
            o = parse.urlparse(self.path)
            path = o.path
            kwargs = parse.parse_qs(o.query)
            for kwarg in kwargs:
                kwargs[kwarg] = kwargs[kwarg][0]
            print("path:"+path+", kwargs:"+str(kwargs))
            response_bytes = self.DirectAPIRegister.handle(path, kwargs)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(response_bytes)
            #self.wfile.write(bytes(self.path, "utf-8"))
            return


class DirectAPIRegister:
    def __init__(self):
        self.handler_function = {}

    def register(self, path, handler_function):
        self.handler_function[path] = handler_function
        
    def handle(self, path, kwarys):
        try:
            response = self.handler_function[path](**kwarys)
        except:
            response = "Failed to handle, check the path or params"
        return bytes(json.dumps(response), "utf-8")
    
