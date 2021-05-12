from application import app, db
from application.models import YogaMove, YogaSequence
from application.forms import TaskForm, TaskFormTwo
from flask import render_template, request, redirect, url_for, session

@app.route("/")
@app.route('/home')
def home():
    all_tasks = YogaMove.query.all()
    all_sequence = YogaSequence.query.all()
    session["current_id"]=None
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
    form = TaskFormTwo(request.form)
    if session.get('current_id'): instructions = session['current_id']
    else: instructions = []
             
    form.instruction.choices = [(move.id, move.description) for move in YogaMove.query.all()]

    if request.method == "POST":
        if form.submit.data:
            if form.validate_on_submit():
                moves = [YogaMove.query.get(id) for id in instructions]
                print(moves)
                sequence = YogaSequence(name=form.name.data, difficulty=form.difficulty.data, time=form.time.data,
                moves=moves)
            #not sure if you can put these both on the same line
                db.session.add(sequence)
                db.session.commit()
                return redirect(url_for("home"))
        if form.add_instruction.data:
            if form.instruction.data:
                instructions.append(form.instruction.data)
                session['current_id'] = instructions
    instructions = [YogaMove.query.get(id).description for id in instructions]

    return render_template("addsequence.html", title="Create a sequence", form=form, instructions=instructions)




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
    return render_template("updatemoves.html", form=form, title="Update Move", task=task)

@app.route("/updatesequences/<int:id>", methods=["GET", "POST"])
def updatesequences(id):
    formTwo = TaskFormTwo()
    task = YogaSequence.query.filter_by(id=id).first()
    if request.method == "POST":
        task.name = formTwo.name.data
        task.time = formTwo.time.data
        task.difficulty = form.difficulty.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("updatesequences.html", formTwo=formTwo, title="Update Sequence", task=task)


@app.route("/delete/<int:id>")
def delete(id):
    task = YogaMove.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/deletesequence/<int:id>")
def deletesequence(id):
    task = YogaSequence.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))