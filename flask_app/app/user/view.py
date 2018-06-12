from app.user import user
import json

user_list = [{
    'id': 1,
    'name': 'pgz',
    'age': 20
}, {
    'id': 2,
    'name': 'admin',
    'age': 18
}]


@user.route('/')
def get_list():
    return json.dumps(user_list)


@user.route('/add')
def add_user():
    return 'add_user'
