from app.ui import ui
from flask import render_template
from app.models import Curso, Actividad


@ui.route("/")
def index():
    cursos = Curso.query.all()
    return render_template("index.html", cursos=cursos)

@ui.route("/actividades")
def actividades():
    actividades = Actividad.query.all()
    return render_template("actividades.html", actividades=actividades)
