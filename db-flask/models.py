from app import db

class Person(db.Model):
    __tablename__ = 'people'
    
    pid = db.Column(db.Intger,primary_key=True)
    name = db.Column(db.Text,)