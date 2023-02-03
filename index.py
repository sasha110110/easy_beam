from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, RadioField, StringField
from wtforms.validators import DataRequired,EqualTo, ValidationError, InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kek'

@app.route('/', methods=['GET', 'POST'])
def display():
    return render_template("index.html")
    
  
