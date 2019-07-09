from flask import Flask
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = "5TR4NG3R-TH1NGS"


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class User(UserMixin):
  def __init__(self,id):
    self.id = id


@app.route('/')
def home():
    return "home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>"


@app.route('/protected/')
@login_required
def protected():
    return "protected"


@app.route('/login/')
def login():
    login_user(User(1))
    return "login deployed successfully"


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return "session complete"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1212, debug=True)

