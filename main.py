from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm as Form
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange
from calculate import is_leap_year, next_five_leap

app = Flask(__name__)
app.secret_key = '\xed\xc3\xb3H\xb4\xb39/LI\x15Q\xaf\xf9mz\x08\x1a\x926\xa2\xabc*'


class YearForm(Form):
    year = IntegerField(
        'Year',
        validators=[DataRequired(), NumberRange(min=1582, max=2800)]
    )


@app.route('/', methods=['GET', 'POST'])
def home():
    year_form = YearForm()
    if year_form.validate_on_submit():
        flash('Validated')
        year = year_form.year.data
        return render_template(
            'home.html',
            form=year_form,
            result_is_leap_year=is_leap_year(year),
            result_next_five_year=[year+i for i in range(1, 6)],
            result_next_five_leap=next_five_leap(year)
        )
    return render_template('home.html', form=year_form)
