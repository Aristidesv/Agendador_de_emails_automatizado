import time
from datetime import datetime
from database import listar_emails, marcar_como_enviado
import smtplib
from email.mime.text import MIMEText

SEU_EMAIL = "Seu_email_@gmail.com"
SENHA = "Senha_do_Gerada"

def enviar_email(destinatario, assunto, mensagem):
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = SEU_EMAIL
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SEU_EMAIL, SENHA)
        server.send_message(msg)
        print(f"E-mail enviado para {destinatario}")

def verificar_agendados():
    while True:
        emails = listar_emails()
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")

        for email in emails:
            email_id, dest, assunto, mensagem, data_envio, status = email
            if status == 'agendado' and data_envio.strip() == agora:
                try:
                    enviar_email(dest, assunto, mensagem)
                    marcar_como_enviado(email_id)
                except Exception as e:
                    print(f"Erro ao enviar: {e}")
        time.sleep(60)

if __name__ == '__main__':
    verificar_agendados()