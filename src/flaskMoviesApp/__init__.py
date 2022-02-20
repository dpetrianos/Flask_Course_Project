from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from datetime import timedelta
from flask_login import LoginManager

app = Flask(__name__) # create your Flask application

### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'


app.config["SECRET_KEY"] = 'b668cbc68d29fd2b7f5976c54c39f6ec'
app.config['WTF_CSRF_SECRET_KEY'] = 'fe9d487ba2c9a1f13a5d72fa0d76d3fb'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_movies_database.db"    # load the configuration of choice
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=10)

### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = SQLAlchemy(app)  ## create the SQLAlchemy object by passing it the application

bcrypt = Bcrypt(app) ##

login_manager = LoginManager(app) ##

login_manager.login_view = "login_page" ##
login_manager.login_message_category = "warning" ##
login_manager.login_message = "Παρακαλόύμε κάντε login για να μπορέσετε να δείτε αυτή τη σελίδα." ##


from src.flaskMoviesApp import routes, models



