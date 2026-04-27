from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks [cite: 10]
tasks = []

# HTML Template for the interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Python To-Do App</h2>
    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter a new task" required>
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>
                {{ task.content }} 
                <a href="/delete/{{ loop.index0 }}">[Delete]</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append({'content': task_content, 'completed': False}) # Add a new task [cite: 9]
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id) # Delete a task [cite: 11]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
