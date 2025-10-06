from flask import Flask
from flask_restx import Api
from models import db
from controllers.professor import ns as professor_ns
from controllers.turma import ns as turma_ns
from controllers.aluno import ns as aluno_ns
import os

def create_app():
    app = Flask(__name__)

    # Caminho absoluto para o arquivo do banco de dados
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco
    db.init_app(app)

    # Configuração da documentação Swagger
    api = Api(
        app,
        version="1.0",
        title="API Escolar - Flask MVC",
        description="Gerenciamento de Professores, Turmas e Alunos"
    )

    # Registra os namespaces (rotas)
    api.add_namespace(professor_ns)
    api.add_namespace(turma_ns)
    api.add_namespace(aluno_ns)

    # Cria as tabelas no banco (se ainda não existirem)
    with app.app_context():
        db.create_all()

    return app


# Executa o servidor Flask
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
