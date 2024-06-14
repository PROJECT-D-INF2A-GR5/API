from flask_restful import Resource, reqparse
from init import customer_service, db
from crud.database_crud import DatabaseCrud
from dotenv import dotenv_values
import psycopg2

class Conversation(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_id", type=str, required=True)
        con = "dbname='ProjectD' user='postgres' password='1234' host='localhost' port='5432'"
        self.database_crud = DatabaseCrud(con)

    def post(self, user_id):
        self.parser.add_argument("user_message", type=str)
        args = self.parser.parse_args(strict=True)

        # todo - Retrieve a list of the past conversation
        past_conversation = []
        message = [{"role":"user", "content":args["user_message"]}]

        conversation = customer_service.initial_conversation + past_conversation + message
        # todo- Also add the message to the database
        # db.session.add(conversation)

        reply = customer_service.get_reply(conversation)
        # todo - Also add the reply to the database
        # db.session.add(reply)

        # commit changes to database
        # db.session.commit()

        return reply
    
    def get(self, user_id):
        conversation = self.database_crud.get_conversation(user_id)
        conversation.insert(0, customer_service.get_initial_message())

        return conversation