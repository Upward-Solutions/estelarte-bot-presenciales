flask-api-cursos/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── db.py
├── migrations/
├── config.py
├── .env
├── requirements.txt
└── run.py


flask db init
flask db migrate -m "Initial migration"
flask db upgrade
