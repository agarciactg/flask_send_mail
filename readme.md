# Flask Email Sender

Este proyecto es una aplicación Flask que expone un endpoint tipo POST para enviar correos electrónicos desde una cuenta específica.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Navega al directorio del proyecto en tu terminal.

3. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. Instala las dependencias:
    ```bash
    pip install Flask
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

2. La aplicación se ejecutará en `http://127.0.0.1:5000/`.

## Endpoint

### POST `/send-email`

Este endpoint envía un correo electrónico utilizando las credenciales proporcionadas.

#### Solicitud

- URL: `http://127.0.0.1:5000/send-email`
- Método: `POST`
- Encabezado: `Content-Type: application/json`
- Cuerpo:

```json
{
  "sender_email": "tu_email@gmail.com",
  "sender_password": "tu_contraseña",
  "recipient_email": "destinatario@example.com",
  "subject": "Asunto del correo",
  "body": "Cuerpo del correo"
}
