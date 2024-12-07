from common.__init__ import app, auth
from flask import request


@app.route('/', methods =['GET'])
def index():
    return 'hello'

@app.route('/addUser', methods =['POST'])
@auth.login_required
def add_user():
    return 'hello'


@app.route('/getUser', methods =['GET'])
@auth.login_required
def get_user():
    return 'hello'


@app.route('/searchUser/<username>', methods =['GET'])
@auth.login_required
def search_user():
    return 'hello'
