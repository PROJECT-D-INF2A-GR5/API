from crud_interface import CrudABC
from database.models import Conversation, Message, User
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import datetime
import math

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
            return conversation.id

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    
    def get_messages(self, conversation_id):
        session = self.Session()
        try:
            # Query to retrieve the messages
            messages = session.query(Message).filter(Message.conversation_id == conversation_id).all()

            messagelist = []

            for message in messages:
                messagelist.append({"role": message.role, "content": message.content})
            return messagelist
        

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def add_message(self, conversation_id, message):
        session = self.Session()
        try:
            # Add message to the database
            
            max_id = session.query(Message.id).all()
            max_id = max(max_id)[0] if max_id else 0

            new_message = Message(id=max_id+1,
                                    created_on=datetime.datetime.now(),
                                    modified_on=datetime.datetime.now(),
                                    deleted_on=None,
                                    conversation_id=conversation_id,
                                    role=message["role"],
                                    content=message["content"])
            session.add(new_message)
            session.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()
    
    def get_max_id(self):
        session = self.Session()
        try:
            max_id = session.query(User.id).all()
            max_id = max(max_id)[0] if max_id else 0
            return max_id

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def create_user(self, user_id):
        session = self.Session()
        try:
            # Create a new user

            new_user = User(id=user_id,
                            created_on=datetime.datetime.now(),
                            modified_on=datetime.datetime.now(),
                            deleted_on=None)
            session.add(new_user)

            max_id = session.query(Conversation.id).all()
            max_id = max(max_id)[0] if max_id else 0

            new_conversation = Conversation(id=max_id+1,
                                            created_on=datetime.datetime.now(),
                                            modified_on=datetime.datetime.now(),
                                            deleted_on=None,
                                            user_id=user_id)
            session.add(new_conversation)
            session.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()