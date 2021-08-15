
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This is mandatory field and can not be left blank..")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This is mandatory field and can not be left blank..")

    def post(self):
        result = UserRegister.parser.parse_args()

        if UserModel.find_by_username(result['username']):
            return {"message": "An user with that username already exists"}, 400

        user = UserModel(**result)
        user.save_to_db()

        return {"message": "Use is created successfully"}, 201
