from flask import render_template, url_for, redirect, flash, Response, jsonify, json

from app.models import StudentDetail
from app.forms import StudentDetailsForm, SearchForm, UpdateForm
from app import app, db

depts = {'01': 'Arch', '02': 'Chem', '03': 'Civil', '06': 'Computer Science',
    '07': 'EEE', '08': 'ECE', '10': 'ICE', '11': 'Mech', '12': 'Mettallurgy', '14': 'Production'}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        stud = StudentDetail.query.filter_by(name=form.search.data).first() \
            or StudentDetail.query.filter_by(roll_no=form.search.data).first()
        if stud:
            roll_no = [x for x in stud.roll_no]
            dept = roll_no[1] + roll_no[2]
            if dept in depts.keys():
                stud_dept = depts[dept]
            else:
                stud_dept = ''
        return render_template('index.html', form=form, stud = stud, stud_dept = stud_dept)      
    return render_template('index.html', form=form)

@app.route('/add-student/', methods=['GET', 'POST'])
def add():
    form = StudentDetailsForm()
    if form.validate_on_submit():
        new_stud = StudentDetail(name=form.name.data, roll_no=form.roll_no.data)
        db.session.add(new_stud)
        db.session.commit()
        flash('Student Added')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/removestudent/<stud_id>')
def remove(stud_id):
    if StudentDetail.query.filter_by(id=stud_id).first():
        rem_stud = StudentDetail.query.filter_by(id=stud_id).first()
        db.session.delete(rem_stud)
        db.session.commit()
        flash('Student Removed')
    return redirect(url_for('index'))

@app.route('/updatestudent/<stud_id>', methods=['GET', 'POST'])
def update(stud_id):
    form = UpdateForm()
    if form.validate_on_submit():
        if StudentDetail.query.filter_by(id=stud_id).first():
            upd_stud = StudentDetail.query.filter_by(id=stud_id).first()
            if form.name.data:
                upd_stud.name = form.name.data
            if form.roll_no.data:
                upd_stud.roll_no = form.roll_no.data
            db.session.commit()
            flash('Student Updated')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
    
@app.route('/searchlist')
def searchList():
    studs = StudentDetail.query.all()
    studDetails = []
    for stud in studs:
        studDetails.append(stud.name)
        studDetails.append(stud.roll_no)
    print(studDetails)
    return Response(json.dumps(studDetails), mimetype='application/json')

# for stud in studs:
#         name = {}
#         name['name'] = stud.name
#         roll_no = {}
#         roll_no['roll_no'] = stud.roll_no
#         studDetais.append(name)
#         studDetais.append(roll_no)