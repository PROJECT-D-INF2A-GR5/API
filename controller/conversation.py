from flask_restful import Resource, reqparse
from init import customer_service, db
from crud.database_crud import DatabaseCrud
from dotenv import dotenv_values
from repositories.conversation_repository import ConversationRepository

class Conversation(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_id", type=str, required=True)
        self.database_crud = DatabaseCrud(dotenv_values(".env")["CONNECTION_STRING"])

    def post(self):
        args = self.parser.parse_args(strict=True)
        conversation_repo = ConversationRepository(db.session)
        conversation_repo.create(args["user_id"])
        # self.parser.add_argument("user_message", type=str)
        # args = self.parser.parse_args(strict=True)

        # # todo - Retrieve a list of the past conversation
        # # past_conversation = self.database_crud.get_conversation(user_id)
        # # message = [{"role":"user", "content":args["user_message"]}]

        # # conversation = customer_service.initial_conversation + past_conversation + message
        # # self.database_crud.add_message(user_id, message)

        # #  reply = customer_service.get_reply(conversation)


        # # todo - Also add the reply to the database
        # # db.session.add(reply)

        # # commit changes to database
        # # db.session.commit()

        # return conversation
    
    def get(self, user_id):
        conversation = self.database_crud.get_conversation(user_id)
        messages = self.database_crud.get_messages(conversation)
        messages.insert(0, customer_service.get_initial_message())

        return conversation