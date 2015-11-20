#!/usr/bin/env python3

import http.server
import re
import urllib.parse


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.startswith("/home"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                request_id_regex = re.search(r"/home\?id=(.*)", self.path, re.IGNORECASE)
                if request_id_regex:
                    request_id = urllib.parse.unquote(request_id_regex.group(1))
                else:
                    self.send_error(404)
                
                self.wfile.write(request_id.encode("utf-8"))
            else:
                self.send_error(404)

        except IOError:
            self.send_error(404)

        return


def main():
    try:
        server = http.server.HTTPServer(('', 8080), MyHandler)
        print("Serveur démarré.")
        server.serve_forever()
    except KeyboardInterrupt:
        print('Interruption du serveur.')
        server.socket.close()


if __name__ == "__main__":
        main()
