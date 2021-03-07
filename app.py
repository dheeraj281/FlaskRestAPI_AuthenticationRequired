from API_call import api
from API_call.booksAPI import ALL_BOOK,ONE_BOOK
from API_call.user_api import User_registration
from flask_jwt import JWT
from API_call import app
from API_call.secure_check import authenticate, identity

jwt = JWT(app, authenticate, identity)

api.add_resource(User_registration, '/register')
api.add_resource(ALL_BOOK,'/books')
api.add_resource(ONE_BOOK,'/books/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
