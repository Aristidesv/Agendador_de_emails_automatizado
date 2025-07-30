from flask import Flask, request, render_template_string, redirect #os passos para instalar as bibliotecas estao no doc.txt
from database import criar_tabela, inserir_email, listar_emails

app = Flask(__name__)
criar_tabela()

HTML_TEMPLATE = """
<!doctype html>
<html lang="pt">
<head>
  <meta charset="utf-8">
  <title>Agendador de E-mails</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
  <h1 class="mb-4">Agendador de E-mails</h1>
  <form method="post" class="mb-5">
    <div class="mb-3">
      <label class="form-label">Destinatário</label>
      <input type="email" name="destinatario" class="form-control" required>
    </div>
    <div class="mb-3">
      <label class="form-label">Assunto</label>
      <input type="text" name="assunto" class="form-control" required>
    </div>
    <div class="mb-3">
      <label class="form-label">Mensagem</label>
      <textarea name="mensagem" class="form-control" required></textarea>
    </div>
    <div class="mb-3">
      <label class="form-label">Data e hora (DD/MM/YYYY HH:MM)</label>
      <input type="text" name="data_envio" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">Agendar</button>
  </form>

  <h2>Lista de E-mails</h2>
  <table class="table table-striped">
    <thead><tr><th>Destinatário</th><th>Assunto</th><th>Mensagem</th><th>Data de Envio</th><th>Status</th></tr></thead>
    <tbody>
    {% for email in emails %}
      <tr>
        <td>{{ email[1] }}</td>
        <td>{{ email[2] }}</td>
        <td>{{ email[3] }}</td>
        <td>{{ email[4] }}</td>
        <td>{{ email[5] }}</td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inserir_email(
            request.form['destinatario'],
            request.form['assunto'],
            request.form['mensagem'],
            request.form['data_envio']
        )
        return redirect('/')
    emails = listar_emails()
    return render_template_string(HTML_TEMPLATE, emails=emails)

if __name__ == '__main__':
    app.run(debug=True)