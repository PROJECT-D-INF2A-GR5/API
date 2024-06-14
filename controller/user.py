from flask_restful import Resource, reqparse
from crud.database_crud import DatabaseCrud
from dotenv import dotenv_values

class User(Resource):

    def __init__(self):
        self.database_crud = DatabaseCrud(dotenv_values(".env")["CONNECTION_STRING"])

    def post(self, user):
        self.parser.add_argument("user_message", type=str)
        args = self.parser.parse_args(strict=True)

        return
    
    def get(self, user):
        if user == 'get_max_id':
            return self.database_crud.get_max_id()+1
        else:
            return {'error': 'Invalid action'}, 400