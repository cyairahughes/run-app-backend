from flask import request
import account_services
from common.__init__ import app, auth


@app.route('/signup', methods =['POST'])
def create_account():
    return account_services.create_account(request.json)


@app.route('/login', methods =['POST'])
def login():
    return account_services.verify_login(request.json)


@app.route('/changeUsername', methods=['PUT'])
@auth.login_required
def change_username():
    return account_services.update_username(auth.current_user(), request.json)


@app.route('/changePassword', methods=['PUT'])
@auth.login_required
def change_password():
    return account_services.update_password(auth.current_user(), request.json)


@app.route('/deleteAccount', methods=['DELETE'])
@auth.login_required
def delete_account():
    return account_services.delete_account(auth.current_user())