from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), nullable=False)
    pw_hash = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(64), nullable=True)    # users can register without an email

    accounts = db.relationship('Account', backref='owner', lazy='dynamic')
    shares = db.relationship('Share', backref='owner', lazy='dynamic')

    def __init__(self, uid, name, pw, email=None):
        self.user_id = uid
        self.user_name = name
        self.pw_hash = pw
        self.user_email = email

    def __repr__(self):
        return '<User {} - {}>'.format(self.user_id, self.user_name)
    

class Account(db.Model):
    acc_id = db.Column(db.Integer, primary_key=True)
    acc_name = db.Column(db.String(32), nullable=False)
    acc_age = db.Column(db.Integer, nullable=False)
    acc_total = db.Column(db.Double, nullable=False)

    acc_holder = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, aid, name, total):
        self.acc_id = aid
        self.acc_name = name
        self.acc_age = 0
        self.acc_total = total

    def __repr__(self):
        return '<Account {} - ${}>'.format(self.acc_id, self.acc_total)

class Share(db.Model):
    stock_id = db.Column(db.String(5), primary_key=True)
    stock_name = db.Column(db.String(32), nullable=False)
    stock_value = db.Column(db.Double, nullable=False)
    num_shares = db.Column(db.Double, nullable=False)
    avg_price = db.Column(db.Double, nullable=False)

    share_holder = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, sid, name, val, num, avg):
        self.stock_id = aid
        self.stock_name = name
        self.stock_value = val
        self.num_shares = num
        self.avg_price = avg

    def __repr__(self):
        return '<Stock {} - {} shares @ ${} - Current ${}>'.\
            format(self.stock_id, self.num_shares, self.avg_price, self.stock_value)


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(32), nullable=False)
    task_is_expense = db.Column(db.Boolean, nullable=False)     # if False, task is income
    task_amount = db.Column(db.Double, nullable=False)

    def __init__(self, tid, name, exp, amount):
        self.task_id = tid
        self.task_name = name
        self.task_is_expense = exp
        self.task_amount = amount

    def __repr__(self):
        return '<Task {} - {}>'.format(self.task_id, self.task_name)