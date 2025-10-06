import os

class Config:
    # Caminho base do projeto
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    # Caminho completo para o banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(BASEDIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Outras configurações do Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
