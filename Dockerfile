# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y la aplicación a la imagen de Docker
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que la aplicación correrá
EXPOSE 5511

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
