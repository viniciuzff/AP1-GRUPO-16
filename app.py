from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from config import Config

# Inicializa o app Flask
app = Flask(__name__)
app.config.from_object(Config)

# Importa o db do models.py
from models import db
db.init_app(app)

# Cria a API REST
api = Api(
    app,
    title='API Escolar - Grupo 16',
    version='1.0',
    description='Gerenciamento de Professores, Turmas e Alunos'
)

# Importa os controllers (namespaces)
try:
    from controllers.professor import ns as professor_ns
    from controllers.turma import ns as turma_ns
    from controllers.aluno import ns as aluno_ns

    api.add_namespace(professor_ns, path='/professores')
    api.add_namespace(turma_ns, path='/turmas')
    api.add_namespace(aluno_ns, path='/alunos')

except Exception as e:
    print("⚠️ Aviso: falha ao importar controllers:", e)

# Cria as tabelas do banco automaticamente se não existirem
with app.app_context():
    db.create_all()
    print("✅ Banco verificado (tabelas criadas se necessário).")

# Executa o app
if __name__ == '__main__':
    app.run(debug=True)
