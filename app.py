from flask import Flask, render_template, url_for
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2da0e1db3516e7d0d18800d449a48c8'

posts_data = [
    {
        'author': 'Author 1',
        'title': 'Blog post 1',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'date':datetime.utcnow()
    },
    {
        'author': 'Author 2',
        'title': 'Blog post 2',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'date': datetime.utcnow()

    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts = posts_data)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
    app.run(debug = True)