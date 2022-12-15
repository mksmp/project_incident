from app import db

class Accidents(db.Model):
    __tablename__ = 'accidents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))

    def __repr__(self):
        return '<Accidents: %r>' % self.name


class Types(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Types: %r>' % self.name

accidents_members = db.Table(
    "accidents_members",
    db.Column("accident_id", db.ForeignKey("accidents.id"), primary_key=True),
    db.Column("member_id", db.ForeignKey("members.id"), primary_key=True),
)

class Members(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    member = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Members: {self.member}>'

class Temp_Table(db.Model):
    __tablename__ = 'tmp_tbl'

    id = db.Column(db.Integer, primary_key=True)
    name_tmp = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Members: {self.name_tmp}>'