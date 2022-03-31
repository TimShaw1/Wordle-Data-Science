import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_session import Session
import keyboard

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("home.html", letter="A")
