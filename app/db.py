from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        try:
            # Prueba de conexión a la base de datos
            result = db.session.execute("SELECT 1").fetchone()
            logging.info("✅ Conexión exitosa a la base de datos.")
            print("✅ Conexión exitosa a la base de datos.")
        except Exception as e:
            logging.error(f"❌ Error al conectar a la base de datos: {e}")
            print(f"❌ Error al conectar a la base de datos: {e}")