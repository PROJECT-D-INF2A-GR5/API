from crud_interface import CrudABC
import psycopg2
from psycopg2 import sql

class DatabaseCrud(CrudABC):
    def __init__(self, connection_string):
        super().__init__(connection_string)
        # Initialize database connection using connection_string

    def get_conversation(self, user_id):
        try:
            # Establish connection to the database
            connection = psycopg2.connect(self.connection_string)
            cursor = connection.cursor()

            # Query to retrieve the conversation
            query = sql.SQL("SELECT * FROM conversations WHERE user_id = %s")
            cursor.execute(query, (user_id,))

            # Fetch the result
            conversation = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return self.get_messages(conversation[0])

        except psycopg2.DatabaseError as e:
            print(f"Error: {e}")
    
    def get_messages(self, conversation_id):
        try:
            # Establish connection to the database
            connection = psycopg2.connect(self.connection_string)
            cursor = connection.cursor()

            # Query to retrieve the conversation
            query = sql.SQL("SELECT * FROM messages WHERE conversation_id = %s")
            cursor.execute(query, (conversation_id,))

            # Fetch the result
            messages = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return messages

        except psycopg2.DatabaseError as e:
            print(f"Error: {e}")

    def add_message(self, conversation_id, message):
        # Implementation to add a message to a conversation in the database
        print(f"Added message to conversation {conversation_id}: {message}")