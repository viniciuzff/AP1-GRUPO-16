from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ---------- PROFESSOR ----------
class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    disciplina = db.Column(db.String(80))
    ativo = db.Column(db.Boolean, default=True)

    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def __repr__(self):
        return f"<Professor {self.nome}>"


# ---------- TURMA ----------
class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __repr__(self):
        return f"<Turma {self.descricao}>"


# ---------- ALUNO ----------
class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(20))
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)

    def __repr__(self):
        return f"<Aluno {self.nome}>"
