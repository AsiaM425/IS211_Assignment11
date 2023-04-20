from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

todo_list = []

@app.route('/')
def show_todo_list():
    return render_template('index.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit_todo():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # validate email using regular expression
    email_regex = r"[^@]+@[..^@]+\.[^@]+"
    if not re.match(email_regex, email):
        return redirect(url_for('show_todo_list'))

    # validate priority
    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('show_todo_list'))

    todo_list.append((task, email, priority))
    return redirect(url_for('show_todo_list'))

@app.route('/clear')
def clear_todo_list():
    global todo_list
    todo_list = []
    return redirect(url_for('show_todo_list'))

if __name__ == '__main__':
    app.run()
