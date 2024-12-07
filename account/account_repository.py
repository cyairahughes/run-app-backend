from common.__init__ import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(10), nullable=False)


def add_account(username, password):
    account = Account(username=username, password=password)
    db.session.add(account)
    db.session.commit()


def update_username(account_id, username):
    account = Account.query.get_or_404(account_id)
    account.username = account.username if username is None else username
    db.session.add(account)
    db.session.commit()

def update_password(account_id, password):
    account = Account.query.get_or_404(account_id)
    account.password = account.password if password is None else password
    db.session.add(account)
    db.session.commit()
  

def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    return account


def find_account_by_username(username):
    return Account.query.filter_by(username=username).first()

