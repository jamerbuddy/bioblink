
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL


app = Flask(__name__)
CORS(app)
mysql = MySQL()

app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = '3306'
app.config['MYSQL_USER'] = 'james'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'bioblink'

mysql.init_app(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT AVG(falling_time - rising_time) as avg_duration FROM blinks")
    response = cursor.fetchall()

    return {"response": response}

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'

@app.route('/blinks')
def hello():
    data = [5.07, 3.45, 2.67]
    return {"data": data}