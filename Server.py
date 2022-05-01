from http.server import BaseHTTPRequestHandler, HTTPServer
from Football import *
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))

        body = f"<p>{jsonTeams}.</p>"

        self.wfile.write(bytes(body, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":

    path = "D:\\Data\\users\\omer-t\\Desktop\\PlayersEnglish.csv"
    f = Football(path)
    f.read_CSV(f.path_to_file)
    f.create_gorups()
    retry = 0

    while not f.validate_teams() and retry != 100:
        f.clear()
        f.create_gorups()
        retry += 1
    f.create_GK()
    f.print_teams_full()
    f.who_play_first()
    print("======================================")

    jsonTeams = f.teams_to_JSON()
    print(jsonTeams)

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
