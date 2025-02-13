class DBConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        # Beispielverbindung (ersetzen Sie dies mit einer echten Datenbankverbindung)
        self.connection = "Mocked DB Connection"
        print("Connected to the database")

    def execute_query(self, query, params=None):
        # Beispiel-Query-Ausführung
        if query.startswith("SELECT"):
            return [{"id": 1, "email": "user@example.com", "password": "hashed_password"}]
        return "Query executed"
