from http.HttpHandler import HttpHandler
from database.DBConnection import DBConnection
from security.JWTManger import JWTManger
from security.FormatCheck import FormatCheck

handler = HttpHandler()
handler.handle_request()
def main():
    db_connection = DBConnection()
    db_connection.connect()

    http_handler = HttpHandler(db_connection)

    @http_handler.route("/user", methods=["GET"])
    def get_user():
        return http_handler.handle_request("GET_USER")
    http_handler.start()

if __name__ == "__main__":
    main()
