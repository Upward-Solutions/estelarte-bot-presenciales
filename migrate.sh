#!/bin/bash

# Función para verificar si la base de datos está lista
esperar_bd() {
    echo "Esperando a que la base de datos esté lista..."
    until docker exec bot-presenciales-db pg_isready -U postgres > /dev/null 2>&1; do
        sleep 1
    done
    echo "La base de datos está lista."
}

# Menú interactivo
echo "Selecciona el entorno para ejecutar las migraciones:"
echo "1) Local"
echo "2) Producción"
read -p "Opción: " opcion

if [ "$opcion" == "1" ]; then
    # Configuración local
    export FLASK_APP=run.py
    export DATABASE_URL=postgresql://postgres:1234@localhost:5432/bot-presenciales
    echo "Entorno seleccionado: LOCAL"
    esperar_bd
elif [ "$opcion" == "2" ]; then
    # Configuración producción
    export FLASK_APP=run.py
    export DATABASE_URL=postgresql://estelarte_bot_db_user:LkMUwzEL7eCuCumJ2dPuSDZfI3rP2Bz5@dpg-ctuv5npu0jms73aqgorg-a.oregon-postgres.render.com/estelarte_bot_db
    echo "Entorno seleccionado: PRODUCCIÓN"
    esperar_bd
else
    echo "Opción inválida. Saliendo..."
    exit 1
fi

# Realiza las migraciones
echo "Iniciando migraciones..."
flask db init || echo "Ya inicializado, omitiendo 'flask db init'"
flask db migrate -m "Aplicando migraciones iniciales"
flask db upgrade

echo "Migraciones completadas con éxito."
