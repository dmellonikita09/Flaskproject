from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '97924718a878ea65af465d4656b51eb5'

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')