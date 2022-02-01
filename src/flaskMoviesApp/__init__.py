from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from datetime import timedelta
from flask_login import LoginManager

app = Flask(__name__) 


### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'

# CREATE TABLE "article" (
# 	"id"	INTEGER NOT NULL,
# 	"article_title"	VARCHAR(50) NOT NULL,
# 	"article_body"	TEXT NOT NULL,
# 	"article_image"	VARCHAR(30) NOT NULL,
# 	"date_created"	DATETIME NOT NULL,
# 	"user_id"	INTEGER NOT NULL,
# 	PRIMARY KEY(id),
# 	FOREIGN KEY(user_id) REFERENCES user (id)
# );

# CREATE TABLE "user" (
# 	"id"	INTEGER NOT NULL,
# 	"username"	VARCHAR(15) NOT NULL UNIQUE,
# 	"email"	VARCHAR(150) NOT NULL UNIQUE,
# 	"password"	VARCHAR(36) NOT NULL,
# 	"profile_image"	VARCHAR(30),
# 	PRIMARY KEY("id")
# );

# CREATE TABLE "movies" (
# 	"id"	INTEGER NOT NULL,
# 	"title"	VARCHAR(50) NOT NULL,
# 	"plot"	TEXT NOT NULL,
# 	"image"	VARCHAR(40) NOT NULL,
# 	"rating"	INTEGER NOT NULL,
# 	"release_year"	INTEGER NOT NULL,
# 	"date_created"	DATETIME NOT NULL,
# 	"user_id"	INTEGER NOT NULL,
# 	PRIMARY KEY("id"),
# 	FOREIGN KEY("user_id") REFERENCES "user"("id")
# );

app.config["SECRET_KEY"] = 'b668cbc68d29fd2b7f5976c54c39f6ec'
app.config['WTF_CSRF_SECRET_KEY'] = 'fe9d487ba2c9a1f13a5d72fa0d76d3fb'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_movies_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=10)

### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = SQLAlchemy(app)  ##

bcrypt = Bcrypt(app) ##

login_manager = LoginManager(app) ##

login_manager.login_view = "login_page" ##
login_manager.login_message_category = "warning" ##
login_manager.login_message = "Παρακαλόύμε κάντε login για να μπορέσετε να δείτε αυτή τη σελίδα." ##


from flaskMoviesApp import routes, models



