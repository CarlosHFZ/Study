# Enviando E-mails SMTP com Python
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho arquivo HTML
PATH_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
sender = os.getenv('FROM_EMAIL', '')
recipient = sender

# Configurações SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(PATH_HTML, 'r', encoding='utf8') as file:
    text_file = file.read()
    template = Template(text_file)
    text_email = template.substitute(nome='Carlos')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'Este é o assunto do e-mail'

body_email = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(body_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
