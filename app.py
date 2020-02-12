from flask import Flask
import pandas as pd

sys.path.append('../')
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello world!</h1>
    <a href="/about"> Go about </a> 
    """

@app.route('/about')
def about():
    return "<h1>About page!</h1>"

if __name__ == '__main__':
    app.run(debug = True)