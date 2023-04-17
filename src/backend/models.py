import enum
from flask_sqlalchemy import SQLAlchemy

# database object
db = SQLAlchemy()


# ---------------- DATABASE MODELS
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(32), nullable=False)
    pw_hash = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), nullable=False)

    accounts = db.relationship('Account', backref='owner', lazy='dynamic')
    shares = db.relationship('Share', backref='owner', lazy='dynamic')

    def __init__(self, name, pw, email):
        self.user_name = name
        self.pw_hash = pw
        self.user_email = email

    def serialize(self):
        return {'id': self.user_id, 'name': self.user_name}

    # debug
    def __repr__(self):
        return '<User {} - {}>'.format(self.user_id, self.user_name)
    

class Account(db.Model):
    acc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    acc_name = db.Column(db.String(32), nullable=False)
    acc_age = db.Column(db.Integer, nullable=False)     # time since account creation
    acc_total = db.Column(db.Double, nullable=False)

    acc_holder = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, name, total):
        self.acc_name = name
        self.acc_age = 0
        self.acc_total = total

    def serialize(self):
        return {'id': self.acc_id, 'name': self.acc_name, 'age': self.acc_age}

    def __repr__(self):
        return '<Account {} - ${}>'.format(self.acc_id, self.acc_total)


class Share(db.Model):
    stock_id = db.Column(db.String(5), primary_key=True)
    stock_name = db.Column(db.String(32), nullable=False)
    stock_value = db.Column(db.Double, nullable=False) # current stock price
    num_shares = db.Column(db.Double, nullable=False)  # current shares held
    avg_price = db.Column(db.Double, nullable=False)   # price of stock at different purchase times (if > 1), weighted by num_shares purchased

    share_holder = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, sid, name, val, num, avg):
        self.stock_id = sid
        self.stock_name = name
        self.stock_value = val
        self.num_shares = num
        self.avg_price = avg

    def serialize(self):
        return {'id': self.stock_id, 'name': self.stock_name, 'value': self.stock_value}

    def __repr__(self):
        return '<Stock {} - {} shares @ ${} - Current ${}>'.\
            format(self.stock_id, self.num_shares, self.avg_price, self.stock_value)

# for specifying unit of time
class Unit(enum.Enum):
    minute = 1
    hour = 2
    day = 3
    week = 4

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(32), nullable=False)
    task_is_expense = db.Column(db.Boolean, nullable=False)     # if False, task is projected income (expense if True)
    task_amount = db.Column(db.Double, nullable=False)

    # notification settings for scheduled events
    notify = db.Column(db.Boolean, nullable=False)
    notify_unit = db.Column(db.Enum(Unit), nullable=True)
    notify_time = db.Column(db.Double, nullable=True)

    def __init__(self, name, exp, amount, notify):
        self.task_name = name
        self.task_is_expense = exp
        self.task_amount = amount
        self.notify = notify

    def serialize(self):
        return {'id': self.task_id, 'name': self.task_name}

    def __repr__(self):
        return '<Task {} - {}>'.format(self.task_id, self.task_name)