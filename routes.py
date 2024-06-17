from init import api
from controller import test_db, user

api.add_resource(test_db.TestDB, "/testdb/<string:db_type>", methods=["GET"])
api.add_resource(user.User, "/user", methods=["GET"])
