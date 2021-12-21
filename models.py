from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vlad@localhost/interview'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role id={} name={}>'.format(self.role_id, self.name)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    surname = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))

    def __repr__(self):
        return '<User {}:{}>'.format(self.username, self.surname)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.password_hash
        # return check_password_hash(self.password_hash, password)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')