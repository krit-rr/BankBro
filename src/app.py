from flask import Flask, request, g, session, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
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
    if 'user_id' in session:
        g.user = User.query.filter_by(user_id=session['user_id']).first()



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


@api.route('/login', methods=['GET', 'POST'])
def login():
    # to fix:
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(user_name=username).first()
        if user is None or not check_password_hash(user.pw_hash, request.form['password']):
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['user_id'] = user.user_id
            return redirect(url_for('home'))

    return render_template('login.html')

@api.route('/register', methods=['GET', 'POST'])
def register():
    # to fix:
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        if User.query.filter_by(user_name=username).first():
            flash('Username already taken!')
            return redirect(url_for('register'))
        if request.form['password'] != request.form['confirm_password']:
            flash('Passwords do not match!')
            return redirect(url_for('register'))
        else:
            new_user = User(username, password, email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@api.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@api.route('/')
def index():
    return render_template('index.html')