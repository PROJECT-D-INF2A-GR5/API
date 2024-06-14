from crud_interface import CrudABC
from database.models import Conversation, Message
import sqlalchemy
from sqlalchemy.orm import sessionmaker

class DatabaseCrud(CrudABC):
    def __init__(self, connection_string):
        super().__init__(connection_string)
        # Initialize database connection using connection_string
        self.engine = sqlalchemy.create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def get_conversation(self, user_id):
        session = self.Session()
        try:
            # Query to retrieve the conversation
            conversation = session.query(Conversation).filter(Conversation.user_id == user_id).first()
            if conversation:
                return self.get_messages(conversation.id)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    
    def get_messages(self, conversation_id):
        session = self.Session()
        try:
            # Query to retrieve the messages
            messages = session.query(Message).filter(Message.conversation_id == conversation_id).all()
            return messages

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def add_message(self, conversation_id, message):
        session = self.Session()
        try:
            # Add message to the database
            new_message = Message(conversation_id=conversation_id, role=message["role"], content=message["content"])
            session.add(new_message)
            session.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()