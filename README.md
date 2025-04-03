# Flask Form Exercise

*Updated in 2025 to include the latest version of Bootstrap-Flask and its nifty form-handling.*

This is a Flask app with:

* An unfinished form, and
* An unfinished function

&mdash; both in the first route in the app.

The exercise is designed to give you *hands-on practice* with Flask-WTF after you've been introduced to the concepts in:

**Python Beginners** [Flask: Web Forms](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html)

## Get ready to do the exercise

1. Download the zipped repo (*this* repo).
2. Unzip and drag the unzipped folder into your Flask projects folder.
3. Activate your virtual environment there.
4. If you have not already done so, install both Flask-WTF and Bootstrap-Flask as instructed [here](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html).
5. Open a new window in your code editor and drag the *flask-form-exercise-master* folder into it.

## Launch the restaurants app

In the Terminal, at the system prompt, run the app:

```bash
python app.py
```

The form doesn't work yet, but click the link to the restaurants page and you'll see a table listing local restaurants (this comes from the included CSV file).

**The goal of the exercise** is for you to modify the file *app.py* so that the form will write complete data for new restaurants into the file *restaurants.csv*.

## Complete the exercise

In the file *app.py*, there are two places where the comments say *Exercise:* &mdash; adding new code in those two places is all that needs to be done to complete the exercise and make the app work.

1. You will need several additional form controls to enter all the data needed for a restaurant. Figure out how to add them correctly. Note that all changes to the form will be done in *app.py* and **NOT in the template.** 

2. You will need to add code in the function `index()` to make submission of the form write a new record (a new line) into *restaurants.csv*. You'll need to open the file for appending (not reading) and use `csv.writer()`.

Learn about: Python and [CSV Files](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html).

Good luck!
