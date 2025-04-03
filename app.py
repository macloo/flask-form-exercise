from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

import csv


app = Flask(__name__)
# Flask-WTF requires an enryption key - the string can be anything
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# ---------------------------------------------------------------------------
# with Flask-WTF, each web form is represented by a class
# "RestForm" can be changed; "(FlaskForm)" cannot
# see the route for "/" to see how this is used
class RestForm(FlaskForm):
    restaurant = StringField('Restaurant name', validators=[DataRequired(), Length(10, 50)])
    submit = SubmitField('Submit')

# Exercise:
# above, in the class, add new form controls for: 
# address, city, state, zip, phone, url, cuisine, price_range
# make price_range a select element with choice of $ to $$$$
# make all fields required except submit
# ---------------------------------------------------------------------------


# all Flask routes are below

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RestForm()
    # Exercise:
    # Make the form write a new row into restaurants.csv
    # with   if form.validate_on_submit()
    return render_template('index.html', form=form)

@app.route('/restaurants')
def restaurants():
    csvfile = open('restaurants.csv', newline='')
    myreader = csv.reader(csvfile, delimiter=',')
    list_of_rows = []
    for row in myreader:
        list_of_rows.append(row)
    csvfile.close()
    return render_template('rest.html',rests=list_of_rows)

# keep this as is
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
