from app import db

class StudentDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    roll_no = db.Column(db.String(16))

    def __repr__(self):
        return f'Name: {name} Roll No: {roll_no}'