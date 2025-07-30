import sqlite3

def criar_tabela():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destinatario TEXT,
            assunto TEXT,
            mensagem TEXT,
            data_envio TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_email(destinatario, assunto, mensagem, data_envio):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO emails (destinatario, assunto, mensagem, data_envio, status) VALUES (?, ?, ?, ?, ?)",
        (destinatario, assunto, mensagem, data_envio, 'agendado')
    )
    conn.commit()
    conn.close()

def listar_emails():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("SELECT * FROM emails ORDER BY data_envio DESC")
    emails = c.fetchall()
    conn.close()
    return emails

def marcar_como_enviado(email_id):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("UPDATE emails SET status = 'enviado' WHERE id = ?", (email_id,))
    conn.commit()
    conn.close()
