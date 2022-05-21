from subprocess import CREATE_NEW_CONSOLE
import sys
from flask import Flask, abort, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:oyinlola@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Todo Title: {self.title} Description: {self.description}'


db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

@app.route('/create', methods=['POST'])
def createTodo():
    title = request.form.get('title','')
    description = request.form.get('description','')

    todo = Todo(title=title, description=description)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/create_with_json', methods=['POST'])
def create_Todo():
    title = request.get_json()['title']
    description = request.get_json()['description']

    error = False
    body = {}
    try:
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        body = {
            'title': todo.title,
            'description': todo.description
        }
    except:
        db.session.rollback()
        error=True
        print(sys.exc_info())
    finally:
        db.session.close()

    if not error:
        return jsonify(body)
    else:
        abort (400)

    

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)