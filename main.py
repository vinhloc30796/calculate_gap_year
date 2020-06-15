from flask import Flask, render_template
from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

@app.route('/')
def home():
    render_template('home.html')
