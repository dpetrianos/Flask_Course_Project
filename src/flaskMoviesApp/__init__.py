from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)


### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'




app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = ##

bcrypt = ##

login_manager = ##

login_manager.login_view = ##
login_manager.login_message_category = ##
login_manager.login_message = ##


from flaskMoviesApp import routes



