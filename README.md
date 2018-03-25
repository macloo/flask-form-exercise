# Flask Form Exercise

This is a Flask app with:

* An unfinished form, and
* An unfinished function

&mdash; both in the first route in the app.

The exercise is designed to give you hands-on practice with Flask-WTF after you've been introduced to the concepts in:

**python-beginners** [Part 4: Forms in Flask](https://github.com/macloo/python-beginners/tree/master/flask/part4_forms)

## Get ready to do the exercise

1. Download the zipped repo (*this* repo).
2. Unzip and drag the unzipped folder into your Flask projects folder.
3. Activate the virtualenv there.
4. If you have not already done so, install both Flask-WTF and Flask-Bootstrap as instructed [here](https://github.com/macloo/python-beginners/tree/master/flask/part4_forms#setup-for-using-forms-in-flask).
5. Open a new window in Atom and drag the *flask-form-exercise-master* folder into it.

## Launch the restaurants app

In the Terminal, at the bash prompt (`$`), run the app:

```bash
python app.py
```

The form doesn't work yet, but click the link to the restaurants page and you'll see a table listing local restaurants.

**The goal of the exercise** is for you to modify the file *app.py* so that the form will write complete data for new restaurants into the file *restaurants.csv*.

## Complete the exercise

In the file *app.py*, there are two places where the comments say *Exercise:* &mdash; adding new code in those two places is all that needs to be done to complete the exercise and make the app work.

1. You will need several additional form controls to enter all the data needed for a restaurant. Figure out how to add them correctly. Note that all changes to the form will be done in *app.py* and NOT in the template.

2. You will need to add code in the function `index()` to make submission of the form write a new record (a new line) into *restaurants.csv*. You'll need to open the file for appending (not reading) and use `csv.writer()`.

[Python 3.6 csv documentation](https://docs.python.org/3/library/csv.html)

Good luck!
