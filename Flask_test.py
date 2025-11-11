from flask import *
from home import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return render_template('prova5.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/new")
def new():
    return render_template('login.html')