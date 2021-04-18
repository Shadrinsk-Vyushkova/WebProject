from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WebProject_secret_key'

@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', title="Начало", form=form)

@app.route('/start', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
    return render_template('start_test.html', title="Начало тестирования", username=name)


class LoginForm(FlaskForm):
    username = StringField('Имя:')
    submit = SubmitField('Начать')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')