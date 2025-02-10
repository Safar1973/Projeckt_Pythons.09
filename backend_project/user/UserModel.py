from interfaces .IModel import IModel

class UserModel(IModel):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def find_by_id(self, user_id):
        # Beispiel-SQL-Abfrage
        query = "SELECT * FROM users WHERE id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        return result[0] if result else None

    def create(self, email, password):
        # Beispiel-SQL-Insert
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.db_connection.execute_query(query, (email, password))
        return "User created"
