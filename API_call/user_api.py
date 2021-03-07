import json
from flask import Response
from flask_restful import Resource, reqparse
from API_call.model import User






class User_registration(Resource):

    def get(self):
        return '{"API Running successfully}'

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help="email cannot be blank!")
        parser.add_argument('username', type=str, required=True, help="username cannot be blank!")
        parser.add_argument('password', type=str, required=True, help="password cannot be blank!")
        # Parse the arguments into an object
        args = parser.parse_args()
        print(args)

        emailAlreadyRegistered = User.query.filter_by(email=args['email']).first()
        if emailAlreadyRegistered is not None:
            data = {'message': 'This email is already registered.'}
            response = Response(response=json.dumps(data), status=200, mimetype='application/json')
            return response

        usernameAlreadyRegistered = User.query.filter_by(username=args['username']).first()
        if usernameAlreadyRegistered is not None:
            data = {'message': 'This username is already registered.'}
            response = Response(response=json.dumps(data), status=200, mimetype='application/json')
            return response

        newuser = User(email=args['email'],username=args['username'], password=args['password'])
        newuser.save_to_db()
        checkuser = User.query.filter_by(email=args['email']).first()

        if checkuser is not None:
            data = {'message': 'Success', 'data': {'email': args['email'], 'username': args['username'], }}
            response = Response(response=json.dumps(data), status=201, mimetype='application/json')
            return response

        else:
            data = {'message': 'Something went wrong. Try again later'}
            response = Response( response=json.dumps(data), status=500 , mimetype='application/json' )
            return response





