from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = b'327b75e980551be9fa2db558af145fb37131712eeca15e4f77746e4e1b51ce13'

from modul import db, Users
from forms import RegisterForm

csrf = CSRFProtect(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')

@app.route('/')
def base():
    return redirect(url_for('register'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        if form.consent_person_data.data==False:
            flash('Пользователь не дал согласие на обработку персональных данных!', 'danger')
            return redirect(url_for('register'))
        else:
            user = Users(username = form.username.data,
                        email = form.email.data,
                        password = form.password.data,
                        birthday = form.birthday.data,
                        consent_person_data=datetime.now())
            db.session.add(user)
            db.session.commit()
            flash('Пользователь сохранен', 'success')
            return redirect(url_for('register'))
    return render_template('users.html', form=form)