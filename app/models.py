from . import db


class Sample(db.Model):
    __tablename__ = 'samples'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    boolean_value = db.Column(db.Boolean, default=False)
    foo_id = db.Column(db.Integer, db.ForeignKey('foos.id'))


class Foo(db.Model):
    __tablename__ = 'foos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    sample = db.relationship('Sample', backref='foo')
