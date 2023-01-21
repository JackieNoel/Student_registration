from Flask_app import app
from flask import render_template, redirect, request, session
from Flask_app.student import Student


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def success():
    students = Student.get_all()
    print(request.form)
    return render_template('/results.html', new_students=students)


@app.route('/create', methods=['POST'])
def create():
    student = Student.save(request.form)
    print(student)
    return redirect('/result')


@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    return render_template('edit_user.html', one_student=Student.edit_user(data))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    student = Student.update(request.form, id)
    return redirect('/result')


@app.route('/go_home')
def go_home():
    students = Student.get_all()
    return render_template('/results.html', new_students=students)


@app.route('/new_registration')
def new_registration():
    return render_template('index.html')


@app.route('/delete_student/<int:id>')
def delete_student(id):
    Student.delete(id)
    return redirect('/result')
