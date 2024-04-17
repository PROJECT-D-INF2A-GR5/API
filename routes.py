from init import api
from controller import Conversation

api.add_resource(Conversation, "/openai/<string:user_id>", methods=["POST", "GET"])