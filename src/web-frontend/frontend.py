from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "app/index.html"
        return SimpleHTTPRequestHandler.do_GET(self)


def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
