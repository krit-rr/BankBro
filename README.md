# BankBro

## For development (to start the application):

### One time:
1. Navigate to the backend folder and type ```$ python3 -m venv .env``` to create a virtual environment named ```.env```
2. Synchronize environments by typing ```$ pip install -r requirements.txt```

### After that:
1. Navigate to the backend folder and type ```$ source .env/bin/activate```
2. Deploy the backend server by typing ```$ flask run```
3. In a separate terminal, navigate to source_bro folder and type ```$ npm start``` (this deploys the front-end)
4. If adding another dependency, update requirements by typing ```$ pip freeze > requirements.txt```
