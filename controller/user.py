from flask_restful import Resource, reqparse
from crud.database_crud import DatabaseCrud
from dotenv import dotenv_values
import traceback

class User(Resource):

    def __init__(self):
        self.database_crud = DatabaseCrud(dotenv_values(".env")["CONNECTION_STRING"])

    def post(self, user):
        self.parser.add_argument("user_message", type=str)
        args = self.parser.parse_args(strict=True)

        return

    def get(self):
        try:
            user_id = int(self.database_crud.get_max_id())+1
            self.database_crud.create_user(user_id)
            return user_id, 200
        except Exception as e:
            print(traceback.format_exc())
            return {'error': str(e)}, 400
        