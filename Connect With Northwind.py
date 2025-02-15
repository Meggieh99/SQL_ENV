import psycopg2


class NorthwindRepository:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect_db(self):
        conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)
        print("Connection Up:)")

    def close_connection(self):
        if self.connection == True:
            self.connection.close()
        print("Connection closed.")


repo = NorthwindRepository('localhost', 'northwind', 'postgres', '')

repo.connect_db()
repo.close_connection()
