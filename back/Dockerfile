FROM python:3.11-slim

# Define la carpeta de trabajo
WORKDIR /app

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY app ./app

# Expone el puerto Flask
EXPOSE 8000

# Comando final: mantiene el proceso corriendo
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8000"]
