# Imagen base
FROM python:3.12-slim

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Establecer variable de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Exponer el puerto para Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
