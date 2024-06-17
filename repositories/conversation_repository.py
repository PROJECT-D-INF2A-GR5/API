from init import db
from database.models import Conversation
from datetime import datetime

class ConversationRepository:
    def __init__(self, session):
        self.session = session

    def create(self, user_id):
        conversation = Conversation(user_id=user_id, created_on=datetime.now(), modified_on=datetime.now())
        self.session.add(conversation)
        self.session.commit()