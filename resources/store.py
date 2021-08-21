from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.store import StoreModel

from db import db



class Store(Resource):
    #parser = reqparse.RequestParser()
    #parser.add_argument("name",
    #                    type=str,
    #                    required=True,
    #                    help="This field can not be left blank")
    #
    #parser = reqparse.RequestParser()


    @jwt_required()
    def get(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message": "Store by that name does not exist"}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'The store by that name already exists!'}, 400
        store=StoreModel(name)
        store.save_to_db()
        return {'name': name}

    def put(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            return {'message': "Store by that name already exists!"}
        store=StoreModel(name)  
        store.save_to_db()
        return {'name': name}

    def delete(self, name):
        store=StoreModel.find_by_name(name)
        if not store:
            return {'message': 'The store by that name does not exist!'}
        store.delete_from_db()
        return {'message': 'Store deleted!'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}



