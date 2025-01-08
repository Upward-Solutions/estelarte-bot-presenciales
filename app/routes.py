from flask import Blueprint, request, jsonify

from app.db import db
from app.models import Curso, Actividad
from app.schemas import CursoSchema, ActividadSchema

api = Blueprint("api", __name__)
curso_schema = CursoSchema()
cursos_schema = CursoSchema(many=True)
actividad_schema = ActividadSchema()
actividades_schema = ActividadSchema(many=True)


@api.route("/cursos", methods=["GET"])
def get_cursos():
    cursos = Curso.query.all()
    return jsonify(cursos_schema.dump(cursos))


@api.route('/cursos', methods=['POST'])
def create_curso():
    data = request.json  # Obtener datos de la solicitud
    try:
        curso = Curso(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            capacidad=data['capacidad'],
            precio=data['precio']
        )
        db.session.add(curso)
        db.session.commit()
        return jsonify({'id': curso.id}), 201  # Devolver el ID del curso creado con código 201
    except Exception as e:
        db.session.rollback()  # Revertir cambios si hay un error
        return jsonify({'error': str(e)}), 400  # Devolver un error si algo falla


@api.route("/cursos/<int:id>", methods=["PUT"])
def update_curso(id):
    curso = Curso.query.get_or_404(id)
    data = request.json  # Esperamos datos en formato JSON
    try:
        curso.titulo = data.get("titulo", curso.titulo)
        curso.descripcion = data.get("descripcion", curso.descripcion)
        curso.capacidad = data.get("capacidad", curso.capacidad)
        curso.precio = data.get("precio", curso.precio)

        db.session.commit()
        return {"message": "Curso actualizado exitosamente"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


@api.route("/cursos/<int:id>", methods=["DELETE"])
def delete_curso(id):
    curso = Curso.query.get_or_404(id)
    try:
        db.session.delete(curso)
        db.session.commit()
        return {"message": "Curso eliminado exitosamente"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


# CRUD Actividades
@api.route("/actividades", methods=["GET"])
def get_actividades():
    actividades = Actividad.query.all()
    return jsonify(actividades_schema.dump(actividades))


@api.route("/actividades", methods=["POST"])
def create_actividad():
    data = request.json

    # Validar los datos usando el esquema
    errors = actividad_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    # Crear el objeto de la actividad con los datos validados
    actividad = Actividad(
        fecha=data["fecha"],
        horario=data["horario"],
        id_curso=data["id_curso"]
    )

    # Guardar en la base de datos
    db.session.add(actividad)
    db.session.commit()

    # Retornar solo el ID de la actividad creada
    return jsonify({"id": actividad.id}), 201


@api.route("/actividades/<int:id>", methods=["PUT"])
def update_actividad(id):
    # Buscar la actividad por su ID
    actividad = Actividad.query.get_or_404(id)

    # Obtener y validar los datos del request
    data = request.json
    errors = actividad_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    # Actualizar los campos permitidos
    if "fecha" in data:
        actividad.fecha = data["fecha"]
    if "horario" in data:
        actividad.horario = data["horario"]
    if "id_curso" in data:
        actividad.id_curso = data["id_curso"]

    # Guardar los cambios en la base de datos
    db.session.commit()

    # Retornar el ID de la actividad actualizada
    return jsonify({"id": actividad.id}), 200


@api.route("/actividades/<int:id>", methods=["DELETE"])
def delete_actividad(id):
    actividad = Actividad.query.get_or_404(id)
    db.session.delete(actividad)
    db.session.commit()
    return jsonify({"message": "Actividad eliminada"})
