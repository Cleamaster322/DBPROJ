import mysql.connector
class DatabaseManager:
    connection = None

    def __init__(self):
        if not DatabaseManager.connection:
            DatabaseManager.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="789789456qweQ$",
                database="anime"
            )

    def execute_query(self, query, params=None):
        cursor = DatabaseManager.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def execute_update_query(self, query):
        cursor = DatabaseManager.connection.cursor()
        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error updating data: {e}")

    def commit(self):
        DatabaseManager.connection.commit()

    def rollback(self):
        DatabaseManager.connection.rollback()

    def close_connection(self):
        if DatabaseManager.connection:
            DatabaseManager.connection.close()
            DatabaseManager.connection = None