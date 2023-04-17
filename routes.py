from flask import render_template, redirect, url_for, flash, get_flashed_messages
from gsFlask import app, db
from models import Task
import forms
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Task', form.title.data, 'created')

        task = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()

        flash('New task added to database')

        return redirect(url_for('index'))
    return render_template('add.html', form=form)
