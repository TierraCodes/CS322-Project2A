# a minimal Flask app
from flask import Flask, render_template, request, redirect, url_for
from storage import store

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    my_deadlines = store.get_deadlines()
    return render_template('index.html', deadlines = my_deadlines)

@app.route('/add', methods=['GET', 'POST'])
def add_deadline():
    task = request.form.get('task')
    date = request.form.get('date')
    status = request.form.get('status')

    allowed_statuses = ['pending', 'started', 'finished', 'not_started']
    if status not in allowed_statuses:
        status = 'pending'
    if not task or not date:
        return "Error: Missing data", 400

    store.add_deadline(task, date, status)
    return redirect(url_for('home'))


@app.route('/update/<deadline_id>', methods=['POST'])
def update_deadline(deadline_id):
    task = request.form.get('task')
    date = request.form.get('date')
    status = request.form.get('status')

    valid_statuses = ['pending', 'started', 'finished']
    if status not in valid_statuses:
        status = 'pending'

    if task and date:
        store.update(deadline_id, task, date, status)

    return redirect(url_for('home'))

