from http.server import BaseHTTPRequestHandler, HTTPServer
import requests


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """
    @staticmethod
    def __get_contacts():
        """
        Получение скрипта с удаленного репозитория
        """
        contacts = requests.get("https://raw.githubusercontent.com/dipnoe/web_basics/main/index(contacts).html",
                                stream=True, allow_redirects=True)
        return contacts.text

    def do_GET(self):
        """ Метод для обработки GET-запросов """
        self.send_response(200)
        page = self.__get_contacts()
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
