from flask import Flask

api = Flask(__name__)

@api.route('/home', methods=['GET'])
def home():
    response_body = {
        "name": "Bank Bro",
        "about" : "Manage your finance and track stocks"
    }
    return response_body