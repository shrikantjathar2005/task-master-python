from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This list acts as our temporary database
tasks = []

@app.route('/')
def home():
    # Show the main page with current tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Get task from the form
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    # Remove task by index
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)