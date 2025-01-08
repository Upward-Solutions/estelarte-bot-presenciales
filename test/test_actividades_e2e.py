import pytest

from app import create_app
from app.db import db


@pytest.fixture
def client():
    app = create_app()
    app.config.from_object("app.config.TestConfig")

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_get_empty_actividades(client):
    response = client.get("/api/actividades")

    assert response.status_code == 200
    assert response.json == []


def test_create_actividad(client):
    # Crear un curso para asociar la actividad
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Aprende los fundamentos de Python",
        "capacidad": 20,
        "precio": 99.99
    }
    response_curso = client.post("/api/cursos", json=curso_data)
    curso_id = response_curso.json["id"]

    # Crear una actividad asociada al curso
    actividad_data = {
        "fecha": "2025-01-01",
        "horario": "10:00 - 12:00",
        "id_curso": curso_id
    }
    response_post = client.post("/api/actividades", json=actividad_data)

    # Verificar la creación de la actividad
    response_get = client.get("/api/actividades")
    assert response_post.status_code == 201
    assert "id" in response_post.json
    assert len(response_get.json) == 1
    assert response_get.json[0]["id"] == response_post.json["id"]
    assert response_get.json[0]["fecha"] == actividad_data["fecha"]
    assert response_get.json[0]["horario"] == actividad_data["horario"]
    assert response_get.json[0]["id_curso"] == curso_id


def test_update_actividad(client):
    # Crear un curso y una actividad inicial
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Aprende los fundamentos de Python",
        "capacidad": 20,
        "precio": 99.99
    }
    response_curso = client.post("/api/cursos", json=curso_data)
    curso_id = response_curso.json["id"]

    actividad_data = {
        "fecha": "2025-01-01",
        "horario": "10:00 - 12:00",
        "id_curso": curso_id
    }
    response_post = client.post("/api/actividades", json=actividad_data)
    actividad_id = response_post.json["id"]

    # Actualizar la actividad
    nuevo_horario = {"horario": "14:00 - 16:00"}
    response_put = client.put(f"/api/actividades/{actividad_id}", json=nuevo_horario)

    # Verificar que la actividad fue actualizada
    response_get = client.get("/api/actividades")
    assert response_put.status_code == 200
    assert response_put.json["id"] == actividad_id
    assert response_get.json[0]["horario"] == "14:00 - 16:00"


def test_delete_actividad(client):
    # Crear un curso y una actividad inicial
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Aprende los fundamentos de Python",
        "capacidad": 20,
        "precio": 99.99
    }
    response_curso = client.post("/api/cursos", json=curso_data)
    curso_id = response_curso.json["id"]

    actividad_data = {
        "fecha": "2025-01-01",
        "horario": "10:00 - 12:00",
        "id_curso": curso_id
    }
    response_post = client.post("/api/actividades", json=actividad_data)
    actividad_id = response_post.json["id"]

    # Eliminar la actividad
    response_delete = client.delete(f"/api/actividades/{actividad_id}")

    # Verificar que la actividad fue eliminada
    response_get_after_delete = client.get("/api/actividades")
    assert response_delete.status_code == 200
    assert response_delete.json["message"] == "Actividad eliminada"
    assert len(response_get_after_delete.json) == 0
