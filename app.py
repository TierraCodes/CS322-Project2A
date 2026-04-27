# a minimal Flask app
from flask import Flask, render_template
from storage import store

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    my_deadlines = store.get_deadlines()
    return render_template('index.html', deadlines = my_deadlines)

