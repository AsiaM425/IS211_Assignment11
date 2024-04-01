from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fake list of To-Do items for testing
todo_list = [
    {"task": "Buy Milk", "email": "example@example.com", "priority": "High"},
    {"task": "Walk the Dog", "email": "test@example.com", "priority": "Medium"}
]

@app.route('/')
def view_todo_list():
    return render_template('todo_list.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit_todo_item():
    # Get form data
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    # Data validation
    if not task or not email or not priority:
        # Redirect back to main controller with error message
        return redirect('/', error='All fields are required')

    # Add new To-Do item to the list
    new_item = {"task": task, "email": email, "priority": priority}
    todo_list.append(new_item)

    # Redirect back to main controller
    return redirect('/')

@app.route('/clear')
def clear_todo_list():
    # Clear the list of To-Do items
    todo_list.clear()

    # Redirect back to main controller
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

