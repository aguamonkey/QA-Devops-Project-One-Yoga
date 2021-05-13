from application import app, db
from application.models import YogaMove, YogaSequence
from application.forms import TaskForm, TaskFormTwo
from flask import render_template, request, redirect, url_for, session

@app.route("/")
@app.route('/home')
def home():
    all_moves = YogaMove.query.all()
    all_sequence = YogaSequence.query.all()
    session["current_id"]=None
    output = ""
    return render_template("index.html", title="Home", all_moves=all_moves, all_sequence=all_sequence)

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
    move = YogaMove.query.filter_by(id=id).first()
    if request.method == "POST":
        move.description = form.description.data
        move.instruction = form.instruction.data
        move.difficulty = form.difficulty.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("updatemoves.html", form=form, title="Update Move", move=move)

@app.route("/updatesequences/<int:id>", methods=["GET", "POST"])
def updatesequences(id):
    formTwo = TaskFormTwo()
    if session.get('current_id'): instructions = session['current_id']
    else: instructions = []

    formTwo.instruction.choices = [(move.id, move.description) for move in YogaMove.query.all()]

    sequence = YogaSequence.query.filter_by(id=id).first()
    if request.method == "POST":
        if formTwo.submit.data:
            moves = [YogaMove.query.get(id) for id in instructions]

            sequence.name = formTwo.name.data
            sequence.time = formTwo.time.data
            sequence.difficulty = formTwo.difficulty.data
            sequence.moves = moves
            db.session.commit()
            return redirect(url_for("home"))
        if formTwo.add_instruction.data:
            if formTwo.instruction.data:
                instructions.append(formTwo.instruction.data)
                session['current_id'] = instructions
    instructions = [YogaMove.query.get(id).description for id in instructions]

    return render_template("updatesequences.html", formTwo=formTwo, title="Update Sequence", sequence=sequence, instructions=instructions, instruction_names=', '.join([instruction.description for instruction in sequence.moves]))


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