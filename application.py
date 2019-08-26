import os

from flask import Flask, session,render_template,request,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/login")    #have to add "login to end of url of server url"
def login():    
    return render_template("loginPage.html")
'''
@app.route("/registration", methods =["POST"])
def registration():
    #get form information
    name = request.form.get("name")
    password = request.form.get("password")
    user = db.execute("INSERT INTO users (name, password) VALUES (:name, :password)", 
                        {"name": name, "password": password})
    users = db.execute("SELECT * FROM users").fetchall()
    db.commit()
    return render_template("loginPage.html" ,users= users ) #"success.html will later change to loginPage.html after testing is done"
'''
@app.route("/success", methods= ["POST"])
def success():
    
    name = request.form.get("name")
    password = request.form.get("password")
   
    if db.execute("SELECT * FROM users WHERE name = :name AND password = :password ",
                        {"name": name, "password": password }).fetchone() is None:
        return render_template("error.html")
    db.commit()
   
    return render_template("success.html", name = name )

@app.route("/logout", methods =["POST"])
def logout():
    session.pop("login", None)
    return redirect(url_for('login'))

'''
@app.route("/logout", methods =["POST"])
def logout():
    db.
    try:
        userId = int(request.form.get("userId"))
    except ValueError:
        return render_template("error.html", message="Invalid user id")
    return render_template("success.html")
'''