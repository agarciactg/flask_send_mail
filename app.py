from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        sender_email = data['sender_email']
        sender_password = data['sender_password']
        recipient_email = data['recipient_email']
        subject = data['subject']
        body = data['body']

        # Crear el contenedor de mensaje
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Conectar al servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Habilitar seguridad TLS
        server.login(sender_email, sender_password)  # Iniciar sesión

        # Enviar el correo
        server.send_message(msg)
        server.quit()

        return jsonify({'message': 'Correo enviado exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
