class USERTable:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        self.db_connection.execute_query(query)
