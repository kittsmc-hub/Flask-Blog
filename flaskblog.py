from flask import Flask,render_template, url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3f00b33a1d3c790c515c3a394c532bc8'

posts = [
    {
        'author' : 'Kitts',
        'title': 'Blogpost 1 ',
        'content': 'First post content',
        'date_posted' :'april 20, 2018'
    },
    {
        'author' : 'Antony',
        'title': 'Blogpost 2 ',
        'content': 'First post content',
        'date_posted' :'april 23, 2019'
    }
   

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)