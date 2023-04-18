from flask import Flask, request, g, session, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from models import db, User, Account, Share, Task   # database models
from flask_cors import CORS
from datetime import date, time

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config.update(dict(
	SECRET_KEY='devkey',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///dbro.db'
))
db.init_app(app)


# clear all models and reinitialize
@app.cli.command('initdb')
def initdb_command():
	db.drop_all()
	db.create_all()

	db.session.commit()
	print('Reinitialized the database.')


def get_user_id(username):
	u = User.query.filter_by(user_name=username).first()
	return u.user_id if u else None

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.filter_by(user_id=session['user_id']).first()



# home page
@app.route('/home', methods=['GET'])
def home():
    response_body = {
        "name": "Bank Bro",
        "about" : "Manage finance & grow wealth"
    }
    return response_body


@app.route('/activity')
def calendar():
    if not g.user:
        return redirect(url_for('index'))

    tasks = Task.query.filter_by(task_owner=g.user.user_id).all()
    return render_template("cal.html", tasks=tasks)


@app.route('/add', methods=['GET', "POST"])
def add():
    if request.method == "POST":
        name = request.form['title']
        
        amount = request.form['amount']
        year, month, day = request.form['date'].split('-')
        dbdate = date(int(year), int(month), int(day))		# turn HTML date into date type SQLAlchemy knows
        hour, minute = request.form['time'].split(':')
        dbtime = time(int(hour), int(minute))
        exp = True
        t = Task(name, dbdate, exp, amount, False, g.user.user_id, time=dbtime) # false is notify
        db.session.add(t)
        g.user.tasks.append(t)
        db.session.commit()
        return redirect(url_for('calendar'))

    return render_template("add.html")

# stock page
@app.route('/portfolio', methods=['GET'])
def portfolio():
    if not g.user:
        return redirect(url_for('index'))
    
    
    return render_template('portfolio.html')


@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')
