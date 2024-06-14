from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from customer_service import CustomerService
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from database.models import Base

app = Flask(__name__)

api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = dotenv_values(".env")["CONNECTION_STRING"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

engine = create_engine(dotenv_values(".env")["CONNECTION_STRING"])
Base.metadata.create_all(engine)

initial_conversation = [
                {"role": "system", "content": "You are an online customer service."},
                {"role": "user", "content": f"Of the following text, convert the wishes into a json containing keys enclosed in single quotes for furniture type, amount of legs, color, material, length, width, height. If there is missing information to complete the json, keep asking questions to get this info. If all values for the keys are obtained, start the reply with the tag @invoice (very important) followed by the json and a message implying what the price will be, but replace the currency sign and numeric value of the price by the tag @price, all in one message (also very important). The most important rule is not to mention the json without those tags. If the customer is satisfied, he/she will say GERONIMO, reply with GERONIMO in capitals"},
                {"role": "system", "content": "okay."},
                {"role": "user", "content": "Start your roleplay, acting as if we never had this conversation."},
                {"role": "system", "content": "Hello, how can I help you?"},
              ]

customer_service = CustomerService(dotenv_values(".env")["OPENAI_KEY"], initial_conversation)