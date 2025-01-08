#!/bin/bash

# Verifica que el contenedor de PostgreSQL esté corriendo
echo "Esperando a que la base de datos esté lista..."
until docker exec bot-presenciales-db pg_isready -U postgres > /dev/null 2>&1; do
    sleep 1
done
echo "La base de datos está lista."

# Realiza las migraciones
echo "Iniciando migraciones..."
flask db init || echo "Ya inicializado, omitiendo 'flask db init'"
flask db migrate -m "Aplicando migraciones iniciales"
flask db upgrade

echo "Migraciones completadas con éxito."
