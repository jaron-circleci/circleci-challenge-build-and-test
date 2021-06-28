from flask import Flask, render_template, request, redirect
from flask.helpers import url_for


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def my_form():
    question = "What is the best CI/CD Tool?"
    circleci_message="CircleCI!"
    if request.method == 'POST':
         return render_template('index.html', circleci_message=circleci_message)

    return render_template('index.html', question=question)


@app.route('/process', methods= ['POST'])
def my_form_post():
        submitButton = request.form.get('Submit')
        if submitButton:
            return redirect(url_for('index'))

    