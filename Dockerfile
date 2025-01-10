# Imagen base
FROM python:3.12-slim

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crear un usuario no root
RUN useradd -m appuser
USER appuser

# Copiar el código de la aplicación
COPY . .

# Establecer variables de entorno
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Exponer el puerto para Flask
EXPOSE 5000

# Comando para iniciar la aplicación con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
