from flask import Flask, request, g, session, redirect, url_for
from models import db, User, Account, Share, Task   # database models

api = Flask(__name__)
api.config.update(dict(
	SECRET_KEY='devkey',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///dbro.db'
))
db.init_app(api)


# clear all models and reinitialize
@api.cli.command('initdb')
def initdb_command():
	db.drop_all()
	db.create_all()

	db.session.commit()
	print('Reinitialized the database.')




# home page
@api.route('/home', methods=['GET'])
def home():
    response_body = {
        "name": "Bank Bro",
        "about" : "Manage your finance and track stocks"
    }
    return response_body

@api.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # logic to check DB and login user

        return redirect(url_for('home'))

    response_body = {}
    return response_body

@api.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # logic for creating acct and add to DB

        return redirect(url_for('login'))
    
    response_body = {}
    return response_body