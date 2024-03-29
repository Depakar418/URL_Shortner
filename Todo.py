from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append(todo)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    todo = request.form['todo']
    todos.remove(todo)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
