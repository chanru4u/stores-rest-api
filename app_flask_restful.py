import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
import os

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

os.environ['FLASK_ENV'] = 'development'
app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL2', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ravi'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = [{"name": "item1"}, {"name": "item2"}, {"name": "item3"}]

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=4998, debug=True)
