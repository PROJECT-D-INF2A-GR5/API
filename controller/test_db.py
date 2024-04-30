from flask_restful import Resource, reqparse
from init import db
from sqlalchemy import text

class TestDB(Resource):

    def get(self, db_type):
        try:
            match db_type:
                case "postgresql":
                    return self.postgresql()

        except Exception as e:
            return f"Failed to connect to {db_type}. Error: {str(e)}"
        
    def postgresql(self):
        result = db.session.execute(text('SELECT version()'))
        db_version = result.scalar()
        return f"Connected to {db_version}"        