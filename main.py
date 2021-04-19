from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, validators, TextField
from data import db_session
from data.tests import Test

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WebProject_secret_key'
db_session.global_init("db/web_project.db")
db_sess = db_session.create_session()

lst_test = []
res = []


@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', title="Начало", form=form)


@app.route('/start', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        test_id = request.form.get('id_test')
        if test_id is None:
            test_id = 0
        else:
            res.append(str(request.form.get('choice_switcher')))
            test_id = int(test_id) + 1

    print(test_id)
    print(res)

    if test_id < 4:
        test = db_sess.query(Test).filter(Test.id == test_id).first()
        lst_test.clear()
        lst_test.append((str(test_id * 2 + 1), test.var1))
        lst_test.append((str(test_id * 2 + 2), test.var2))
        testform = TestForm()
        return render_template('start_test.html', title="Начало тестирования", username=name, form=testform, id_test=test_id)
    else:
        return None
        # Написать выборку из базы результата по ответам
        # resForm = ResForm()
        # return render_template('final.html', title="Начало тестирования", username=name, form=resForm, result=res)


class LoginForm(FlaskForm):
    username = StringField('Имя:')
    submit = SubmitField('Начать')


class TestForm(FlaskForm):
    submit = SubmitField("Продолжить")
    choice_switcher = RadioField("В каждой паре утверждений выберете то, с которым вы больше согласны. "
                                 "Номера выбранных утверждений последовательно запишите. "
                                 "Выбранной вами комбинации цифр соответствует определенный тип личности.",
                                 [validators.Required()],
                                 choices=lst_test
                                )


class ResForm(FlaskForm):
    res = TextField()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')