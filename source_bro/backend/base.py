from flask import Flask, request, g, session, redirect, url_for
from models import db, User, Account, Share, Task   # database models
from flask_cors import CORS

api = Flask(__name__)
CORS(api, origins=["http://localhost:3000"])
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


def get_user_id(username):
	u = User.query.filter_by(user_name=username).first()
	return u.user_id if u else None

@api.before_request
def before_request():
    g.user = None
    if 'username' in session:
        g.user = User.query.filter_by(username=session['username']).first()



# home page
@api.route('/home', methods=['GET'])
def home():
    response_body = {
        "name": "Bank Bro",
        "about" : "Manage finance & grow wealth"
    }
    return response_body

# calendar page
@api.route('/activity', methods=['GET'])
def activity():
    response_body = {
        "name": "Calendar",
        "about" : "View past and future income and expenses"
    }
    return response_body

# stock page
@api.route('/portfolio', methods=['GET'])
def portfolio():
    response_body = {
        "name": "Investing",
        "about" : "Track stock prices and shares"
    }
    return response_body



@api.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(user_name=request.form.username).first()  # fetch login username from frontend <--- TO DO!!
        # determine that username is valid

        # check that password hash matches

        # log user in
        session['user_id'] = user.user_id
        return redirect(url_for('home'))

    response_body = {}
    return response_body

@api.route('/register', methods=['GET','POST'])
def register():
    if g.user:
        return redirect(url_for('home'))

    error = None
    if request.method == 'POST':
        # test that the username is valid and doesn't already exist

        # test that the password is atleast 8 chars, and both passwords match

        # add new user to db with User(user_id, user_name, pw_hash)
        
        return redirect(url_for('login'))
    
    response_body = {}
    return response_body  # response to display register page, including errors