# BankBro

## For development (to start the application):

### One time:
1. Navigate to the backend folder and type ```$ python3 -m venv .env``` to create a virtual environment named ```.env```
2. Synchronize environments by typing ```$ pip install -r requirements.txt```

### After that:
1. Navigate to the backend folder and type ```$ source .env/bin/activate```
2. Deploy the backend server by typing ```$ flask run```

If adding another dependency, update requirements by typing ```$ pip freeze > requirements.txt```
