from flask import render_template, request, redirect, flash
from flask_login import login_required
from models import User, Role

from models import app, db


@app.route('/')
def root():
    return redirect('/login')


@app.route('/home')
# @login_required
def home():
    role = 'user'
    if role == 'admin':  # это хардкод
        return "hello admin"
    elif role == 'user':
        return "hello user"
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        return redirect('/home')
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        # print(request.form['psw'])
        # user = User.query.filter_by(username=request.form['username']).first()
        # проверяем аутентификацию
        # if user.password_hash == request.form['psw']:
        #     return redirect('/home')
        # else:
        #     return redirect('/login')
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
# @login_required
def registration():
    if request.method == 'POST':
        if request.form['psw'] != request.form['psw-repeat']:
            render_template("registration.html")
        user_role = Role.query.filter_by(name='user').first()
        user = User(username=request.form['username'], surname=request.form['surname'],
                    password_hash=request.form['psw'])
        # role=user_role)
        # if User.password_hash==False:

        # hash = generate_password_hash(request.form['psw'])
        # else:
        #     render_template("registration.html")
        db.session.add(user)
        db.session.commit()
        return redirect('/home')

    return render_template("registration.html")


@app.route('/logout')
def logout():
    return 'Logout'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
