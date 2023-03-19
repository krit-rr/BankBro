from flask import Flask
from dbro import db, User, Account, Share

api = Flask(__name__)
api.config.update(dict(
	SECRET_KEY='dev key',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///dbro.db'
))
db.init_app(api)


@api.cli.command('initdb')
def initdb_command():
	db.drop_all()
	db.create_all()

	db.session.commit()

	print('Reinitialized the database.')


@api.route('/home', methods=['GET'])
def home():
    response_body = {
        "name": "Bank Bro",
        "about" : "Manage your finance and track stocks"
    }
    return response_body