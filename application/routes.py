from application import app, db
from application.models import Task
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route('/home')
def home():
    all_tasks = Task.query.all()
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route('/create', methods=["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Task(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("add.html", title="Create a task", form=form)

@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Task.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task = Task.query.filter_by(id=id).first()
    if request.method == "POST":
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title="Update Task", task=task)

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))