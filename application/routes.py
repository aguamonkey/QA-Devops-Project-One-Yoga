from application import app, db
from application.models import YogaMove, YogaSequence
from application.forms import TaskForm, TaskFormTwo
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route('/home')
def home():
    all_tasks = YogaMove.query.all()
    all_sequence = YogaSequence.query.all()
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks, all_sequence=all_sequence)

@app.route('/create', methods=["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            move = YogaMove(description=form.description.data, instruction=form.instruction.data, difficulty=form.difficulty.data)
            #not sure if you can put these both on the same line
            db.session.add(move)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("addmove.html", title="Create a move", form=form)

@app.route('/createsequence', methods=["GET", "POST"])
def createsequence():
    form = TaskFormTwo()
    if request.method == "POST":
        if form.validate_on_submit():
            sequence = YogaSequence(name=form.name.data, difficulty=form.difficulty.data, time=form.time.data)
            #not sure if you can put these both on the same line
            db.session.add(sequence)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("addsequence.html", title="Create a sequence", form=form)

@app.route('/complete/<int:id>')
def complete(id):
    task = YogaMove.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = YogaMove.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task = YogaMove.query.filter_by(id=id).first()
    if request.method == "POST":
        task.description = form.description.data
        task.instruction = form.instruction.data
        task.difficulty = form.difficulty.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title="Update Task", task=task)

@app.route("/delete/<int:id>")
def delete(id):
    task = YogaMove.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))