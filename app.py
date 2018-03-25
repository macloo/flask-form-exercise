from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import csv

app = Flask(__name__)
app.config['DEBUG'] = True

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Flask-Bootstrap requires this line
Bootstrap(app)


# ---------------------------------------------------------------------------
# with Flask-WTF, each web form is represented by a class
# "RestForm" can be changed; "(FlaskForm)" cannot
# see the route for "/" to see how this is used
class RestForm(FlaskForm):
    restaurant = StringField('Restaurant name', validators=[Required()])
    submit = SubmitField('Submit')

# Exercise:
# add: address, city, state, zip, phone, url, cuisine, price_range
# make price_range a select element with choice of $ to $$$$
# make all fields required except submit
# ---------------------------------------------------------------------------


# all Flask routes below

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
    app.run(debug=True)
