from crud_interface import CrudABC
from database.models import Message, User
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import datetime
import traceback

class DatabaseCrud(CrudABC):
    def __init__(self, connection_string):
        super().__init__(connection_string)
        # Initialize database connection using connection_string
        self.engine = sqlalchemy.create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_messages(self, user_id):
        session = self.Session()
        try:
            # Query to retrieve the messages
            messages = session.query(Message).filter(Message.user_id == user_id).all()
            messagelist = []
            for message in messages:
                messagelist.append({"role": message.role, "content": message.content})
            return messagelist
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def add_message(self, user_id, message):
        session = self.Session()
        try:
            # Add message to the database

            new_message = Message(
                                    created_on=datetime.datetime.now(),
                                    modified_on=datetime.datetime.now(),
                                    deleted_on=None,
                                    user_id=user_id,
                                    role=message["role"],
                                    content=message["content"])
            session.add(new_message)
            session.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def create_user(self):
        session = self.Session()
        try:
            # Create a new user
            new_user = User(
                            created_on=datetime.datetime.now(),
                            modified_on=datetime.datetime.now(),
                            deleted_on=None)
            session.add(new_user)
            session.commit()
            return new_user.id

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()