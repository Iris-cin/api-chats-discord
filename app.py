from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import random
import os

app = Flask(__name__)
api = Api(app)

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle pour stocker les clés API
class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), unique=True, nullable=False)

# Liste des URLs d'images de chats
cat_images = [
    "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "https://cdn2.thecatapi.com/images/MTY2ODMyNQ.jpg",
    "https://cdn2.thecatapi.com/images/MTYzNjEyMw.jpg",
    # Ajoutez d'autres URLs ici
]

# Fonction pour générer une clé API
def generate_key():
    return os.urandom(16).hex()

# Endpoint pour obtenir une image de chat aléatoire
class RandomCat(Resource):
    def get(self):
        api_key = request.args.get('api_key')
        if not api_key or not APIKey.query.filter_by(key=api_key).first():
            abort(403, description="Invalid or missing API key")
        return jsonify({"image_url": random.choice(cat_images)})

# Endpoint pour générer une nouvelle clé API
class GenerateKey(Resource):
    def post(self):
        new_key = generate_key()
        db.session.add(APIKey(key=new_key))
        db.session.commit()
        return jsonify({"api_key": new_key})

api.add_resource(RandomCat, '/random-cat')
api.add_resource(GenerateKey, '/generate-key')

# Initialisation de la base de données
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
