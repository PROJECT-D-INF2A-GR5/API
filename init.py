from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from crud.database_crud import DatabaseCrud
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
cors = CORS(app, resources={r"*": {"origins": "*"}})

database_crud = DatabaseCrud(dotenv_values(".env")["CONNECTION_STRING"])

@app.route('/openai/<user_id>', methods=['POST'])
def openai(user_id):
    try:
        user_message = request.json.get('user_message')
        if not user_message:
            raise ValueError('user_message is required')

        # Process user_message here
        past_conversation = database_crud.get_conversation(user_id)
        message = {"role":"user", "content":user_message}

        database_crud.add_message(past_conversation, message)

        return jsonify({'message': f'Received message from user {user_id}: {user_message}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return a 400 status code for bad requests

engine = create_engine(dotenv_values(".env")["CONNECTION_STRING"])
Base.metadata.create_all(engine)

initial_conversation = [
                {"role": "system", "content": '''Spreek alleen nederlands, en beantwoord alleen vragen over keukenbladen en offertes. En beantwoord in 2/3 zinnen maximum.
  Zodra de gebruiker zegt 'ik wil een offerte' zal de chatbot vragen stellen over het keukenblad en een offerte genereren. 
  
  Dit zijn de benodigde variablen:

  Welk van de volgende materialen wilt u gebruiken? (Noble Desiree Grey Matt, Noble Carrara Verzoet, Taurus Terazzo White Verzoet, Taurus Terazzo Black, Glencoe Verzoet)
  Wat is de lengte van het keukenblad in m?
  Wat is de breedte van het keukenblad in m?
  Wilt u een spatrand? (Ja/Nee)
  Wilt u een vensterbank? (Ja/Nee)
  Hoeveel boorgaten wilt u? (0-3)
  Wilt u een WCD (contactdoos)? (Ja/Nee)
  Wilt u een randafwerking? (Ja/Nee) 
  Wilt u een wasbak? (Ja/Nee)
  Wilt u een zeepdispenser? (Ja/Nee)
  Wilt u een achterwand? (Ja/Nee)
  Stel de vragen in deze volgorde en als de antwoorden niet voldoen aan de verwachtingen, vraag dan om een correct antwoord.
  Als alle vragen beantwoordt zijn geef de gebruiker een bericht met de all variablen in een object met de juiste waardes op de volgende manier: 
  BEANTWOORDT ALTIJD NA ALLE VRAGEN OP PRECIES DEZE MANIER HET IS HEEL BELANGRIJK VOOR DE REST VAN DE APPLICATIE DUS LET GOED OP: 
  Dit is uw ingevulde offerte:
  {
    materiaal: '',
    lengte: 0,
    breedte: 0,
    spatrand: true/false,
    vensterbank: true/false,
    boorgaten: 0,
    WCD: true/false,
    randafwerking: true/false,
    wasbak: true/false,
    zeepdispenser: true/false,
    achterwand: true/false,
  }
  BEANTWOORDT NOOIT MET DE VOLGENDE WOORDEN: Dit is uw ingevulde offerte: tenzij de offerte volledig is ingevuld.'''},
                {"role": "user", "content": f"Of the following text, convert the wishes into a json containing keys enclosed in single quotes for furniture type, amount of legs, color, material, length, width, height. If there is missing information to complete the json, keep asking questions to get this info. If all values for the keys are obtained, start the reply with the tag @invoice (very important) followed by the json and a message implying what the price will be, but replace the currency sign and numeric value of the price by the tag @price, all in one message (also very important). The most important rule is not to mention the json without those tags. If the customer is satisfied, he/she will say GERONIMO, reply with GERONIMO in capitals"},
                {"role": "system", "content": "okay."},
                {"role": "user", "content": "Start your roleplay, acting as if we never had this conversation."},
                {"role": "system", "content": "Hello, how can I help you?"},
              ]

customer_service = CustomerService(dotenv_values(".env")["OPENAI_KEY"], initial_conversation)