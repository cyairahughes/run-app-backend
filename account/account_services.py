from common.__init__ import log, app
from werkzeug.security import generate_password_hash, check_password_hash
import account_repository
import jwt
from datetime import datetime, timedelta


def create_account(data):
    if 'username' not in data or 'password' not in data:
        log.debug('Request body missing "username" or "password" fields')
        return 'Request body missing "username" or "password" fields', 400

    if is_verified_user(data.get('username')):
        log.debug('Username already exists')
        return 'Username already exists. Try again.', 409

    account_repository.add_account(data.get('username'), generate_password_hash(data.get('password')))
    log.debug('Account created successfully')
    return 'Account created successfully', 201


def verify_login(data):
    if 'username' not in data or 'password' not in data:
        log.error('Request body missing "username" or "password" fields')
        return 'Request body missing "username" or "password" fields', 400

    log.debug('Attempting to find Account with username "{}"'.format(data.get('username')))
    user = account_repository.find_account_by_username(data.get('username'))

    if user:
        if check_password_hash(user.password, data.get('password')):
            token = jwt.encode(
                {'user_id' : user.id, 'exp' :  datetime.utcnow() + timedelta(minutes=30)},
                app.config['SECRET_KEY'], algorithm='HS256')
            log.debug('Login successful')
            return {'token' : token}, 201
    log.debug('Login failed. Username or Password incorrect')
    return 'Login failed. Username or Password incorrect', 401


def update_username(account_id, data):
    if not account_id:
        log.debug('Unauthorized access to update username')
        return 'Unauthorized', 401

    username = None

    if 'username' in data:
        username = data['username']

    account_repository.update_username(account_id, username)
    log.debug('Username updated successfully')
    return 'Username updated successfully', 200

def update_password(account_id, data):
    if not account_id:
        log.debug('Unauthorized access to update password')
        return 'Unauthorized', 401

    password = None

    if 'username' in data:
        password = data['password']

    account_repository.update_password(account_id, password)
    log.debug('Password updated successfully')
    return 'Password updated successfully', 200


def delete_account(account_id):
    if not account_id:
        log.debug('Unauthorized access to delete account')
        return 'Unauthorized', 401
    account_repository.delete_account(account_id)
    log.debug('Account deleted successfully')
    return 'Account deleted successfully', 200


def is_verified_user(username):
    return account_repository.find_account_by_username(username)