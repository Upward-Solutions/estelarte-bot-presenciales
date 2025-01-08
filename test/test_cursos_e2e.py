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


def test_get_empty_cursos(client):
    response = client.get("/api/cursos")

    assert response.status_code == 200
    assert response.json == []


def test_create_curso(client):
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Aprende los fundamentos de Python",
        "capacidad": 20,
        "precio": 99.99
    }

    response_post = client.post("/api/cursos", json=curso_data)

    response_get = client.get("/api/cursos")
    assert response_post.status_code == 201
    assert "id" in response_post.json
    assert len(response_get.json) == 1
    assert response_get.json[0]["id"] == response_post.json["id"]
    assert response_get.json[0]["titulo"] == curso_data["titulo"]
    assert response_get.json[0]["descripcion"] == curso_data["descripcion"]
    assert response_get.json[0]["capacidad"] == curso_data["capacidad"]
    assert response_get.json[0]["precio"] == curso_data["precio"]


def test_update_curso(client):
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Descripción inicial",
        "capacidad": 20,
        "precio": 99.99
    }
    response_post = client.post("/api/cursos", json=curso_data)
    curso_id = response_post.json["id"]
    nueva_descripcion = {"descripcion": "Descripción actualizada"}

    response_put = client.put(f"/api/cursos/{curso_id}", json=nueva_descripcion)

    response_get = client.get(f"/api/cursos")
    assert response_put.status_code == 200
    assert response_put.json["id"] == curso_id
    assert response_get.json[0]["descripcion"] == "Descripción actualizada"


def test_delete_curso(client):
    curso_data = {
        "titulo": "Curso de Python",
        "descripcion": "Descripción inicial",
        "capacidad": 20,
        "precio": 99.99
    }
    response_post = client.post("/api/cursos", json=curso_data)
    curso_id = response_post.json["id"]

    response_delete = client.delete(f"/api/cursos/{curso_id}")

    response_get_after_delete = client.get("/api/cursos")
    assert response_delete.status_code == 200
    assert response_delete.json["message"] == "Curso eliminado"
    assert len(response_get_after_delete.json) == 0
