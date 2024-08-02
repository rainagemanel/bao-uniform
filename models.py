from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class UniformModel(db.Model):
    __tablename__ = "uniforms"
 
    id = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String())
    course_name = db.Column(db.String())
    type = db.Column(db.String(80))
    stock = db.Column(db.Integer())
    sizes = db.Column(db.String(80))
 
    def __init__(self, dep_name,course_name,type,stock,sizes):
        self.dep_name = dep_name
        self.course_name = course_name
        self.type = type
        self.stock = stock
        self.sizes = sizes
        

 
    def __repr__(self):
        return f"{self.dep_name}:{self.course_name}"