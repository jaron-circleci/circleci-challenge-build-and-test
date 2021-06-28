from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def my_form():
    question = "What is the best CI/CD Tool?"
    return render_template('index.html', question=question)


@app.route('/process', methods=['POST'])
def my_form_post():
    submitButton = request.form.get('Submit')
    circleci_message="CircleCI!"
    if submitButton:
        return render_template('index.html', circleci_message=circleci_message)

    