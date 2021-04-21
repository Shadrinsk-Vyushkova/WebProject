from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, validators, TextField
from data import db_session
from data.tests import Test
from data.results import Result


app = Flask(__name__)
app.config['SECRET_KEY'] = 'WebProject_secret_key'
db_session.global_init("db/web_project.db")
db_sess = db_session.create_session()

lst_test = []
res = []
dct = dict()
StrRes = ""


@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', title="Начало", form=form)


@app.route('/start', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        test_id = request.form.get('id_test')
        choice = request.form.get('choice_switcher')
        if test_id is None:
            test_id = 0
            res.clear()
        else:
            if choice is not None:
                res.append(str(choice))
                test_id = int(test_id) + 1
            else:
                test_id = int(test_id)
    if test_id < 4:
        test = db_sess.query(Test).filter(Test.id == test_id).first()
        lst_test.clear()
        lst_test.append((str(test_id * 2 + 1), test.var1))
        lst_test.append((str(test_id * 2 + 2), test.var2))
        testform = TestForm()
        dct.clear()
        dct['username'] = name
        dct['id_test'] = test_id
        return render_template('start_test.html', title="Начало тестирования", form=testform, dct_test=dct)
    else:
        StrRes = ""
        StrRes = "".join(res)
        print(StrRes)
        result = db_sess.query(Result).filter(Result.result == StrRes).first()
        resForm = ResForm()
        dct.clear()
        dct['username'] = name
        dct['type'] = result.type
        dct['soc_type'] = result.soc_type
        dct['representatives'] = result.representatives
        dct['prof'] = result.prof
        dct['profession'] = result.profession
        return render_template('final.html', title="Результат тестирования", form=resForm, dct_res=dct)


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
    type = StringField()
    soc_type = TextField()
    representatives = StringField()
    prof = StringField()
    profession = StringField()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')