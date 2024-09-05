from flask import Flask
from flask_cors import CORS
# from dotenv import load_dotenv
from .routers.bg_remover import bg_remover
from .routers.save_outfit import save_outfit
from firebase_admin import credentials, firestore, initialize_app

# load_dotenv('src/.env')

def create_app():
    app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate('src/wardrobe-wizard-105dd-firebase-adminsdk.json')
    initialize_app(cred, {
        'storageBucket': 'wardrobe-wizard-105dd.appspot.com'
    })
    
    # db = firestore.client()
    
    app.register_blueprint(bg_remover)
    app.register_blueprint(save_outfit)

    @app.route("/")
    def hello():
        return "Hello, World!"

    return app
