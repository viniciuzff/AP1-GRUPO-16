from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    materia = db.Column(db.String(100), nullable=True)
    idade = db.Column(db.Integer, nullable=True)

    turmas = db.relationship('Turma', backref='professor', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Professor {self.nome}>"


class Turma(db.Model):
    __tablename__ = 'turmas'  # 🔧 Faltava isso!
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))  # 🔧 Corrigido o nome da tabela

    alunos = db.relationship('Aluno', backref='turma', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Turma {self.nome}>"


class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.String(20), nullable=True)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Aluno {self.nome}>"
