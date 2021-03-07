from API_call.model import User


def authenticate(username, password):
    user =  User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        print(user)
        return user

def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.query.filter_by(id=user_id).first()