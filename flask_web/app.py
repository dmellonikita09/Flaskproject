from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '97924718a878ea65af465d4656b51eb5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#db.init_app(app)
#with app.app_context():
 #   db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='item_name', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    day_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
        return f"Post('{self.title}', '{self.day_posted}')"


post = [
    {
        'item_name': 'Green Bottle',
        'title': 'post 1',
        'day_posted': 'saturday',
        'date': '10th feb',
        'content': 'Found a Green colored bottle '
    },
    {
        'item_name': 'Yellow Umbrella',
        'title': 'post 2',
        'day_posted': 'sunday',
        'date': '11th feb',
        'content': 'Found a Yellow colored umbrella'
    }
]

@app.route('/')
def home():
    return render_template('home.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'New account created for {form.username.data}!', 'success!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'niki@gmail.com' and form.password.data == 'niki':
            flash('Successfully Loged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Log In. Please recheck your username and password', 'danger') 
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)