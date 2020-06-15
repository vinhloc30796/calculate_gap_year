from flask import Flask, render_template
from flask_wtf import FlaskForm as Form
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.secret_key = '\xed\xc3\xb3H\xb4\xb39/LI\x15Q\xaf\xf9mz\x08\x1a\x926\xa2\xabc*'


class YearForm(Form):
    year = IntegerField(
        'Year',
        validators=[DataRequired(), NumberRange(min=1582, max=2800)]
    )


@app.route('/')
def home():
    year_form = YearForm()
    return render_template(
        'home.html',
        form=year_form
    )
