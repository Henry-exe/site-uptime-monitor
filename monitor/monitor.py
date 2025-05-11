import requests
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_nv()


SITE = "https://example.com"

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_HOST = "email-smtp.us-east-1.amazonaws.com"
SMTP_PORT = 587

def verificar_site(url):
    try:
        r = requests.get(url, timeout=10)
        return r.status_code == 200
    except Exception:
        return False

def enviar_email():
    msg = EmailMessage()
    msg.set_content(f" O site {SITE} está fora do ar!")
    msg["Subject"] = " Alerta: Site offline"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        print("📨Alerta enviado por e-mail.")


if not verificar_site(SITE):
    print(" Site fora do ar, enviando alerta...")
    enviar_email()
else:
    print(" Site está online.")



 