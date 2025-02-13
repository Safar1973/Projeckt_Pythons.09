from .HttpHandler import HttpHandler # Import the HttpHandler class from the http package
class HttpHandler:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        print("Handling HTTP request")

    def route(self, path, methods):
        def decorator(func):
            # Implementierung des Routings
            pass
        return decorator

    def start_server(self, host, port):
       if __name__ == "__main__":
        handler = HttpHandler()
        handler.handle_request()
        def handle_request(self):
         print("Handling HTTP request")
