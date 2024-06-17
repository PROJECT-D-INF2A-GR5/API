from controller import *
from init import api
from controller import test_db, conversation, user

api.add_resource(test_db.TestDB, "/testdb/<string:db_type>", methods=["GET"])
api.add_resource(conversation.Conversation, "/conversation", methods=["POST", "GET"])
api.add_resource(user.User, "/user/<string:user>", methods=["POST", "GET"])