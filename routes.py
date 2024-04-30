from controller import *
from init import api

api.add_resource(test_db.TestDB, "/testdb/<string:db_type>", methods=["GET"])
api.add_resource(conversation.Conversation, "/openai/<string:user_id>", methods=["POST", "GET"])