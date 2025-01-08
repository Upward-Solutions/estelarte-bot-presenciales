from app.db import db

class Curso(db.Model):
    __tablename__ = "cursos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    capacidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    actividades = db.relationship('Actividad', backref='curso', lazy=True)

class Actividad(db.Model):
    __tablename__ = "actividades"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
