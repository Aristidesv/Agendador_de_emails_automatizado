import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    email = "Seu_email_@gmail.com"
    senha = "Codigo_do_Gmail"  # Esse codigo e gerado pelo Gmail os links estao no doc.txt

    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = email
    msg['To'] = destinatario

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Erro ao enviar:", e)
        return False