from models import db, Professor, Turma, Aluno

# ---------- PROFESSOR ----------
class ProfessorRepository:
    @staticmethod
    def get_all():
        return Professor.query.all()

    @staticmethod
    def get_by_id(id):
        return Professor.query.get(id)

    @staticmethod
    def create(**kwargs):
        p = Professor(**kwargs)
        db.session.add(p)
        db.session.commit()
        return p

    @staticmethod
    def update(prof, **kwargs):
        for key, value in kwargs.items():
            setattr(prof, key, value)
        db.session.commit()
        return prof

    @staticmethod
    def delete(prof):
        db.session.delete(prof)
        db.session.commit()


# ---------- TURMA ----------
class TurmaRepository:
    @staticmethod
    def get_all():
        return Turma.query.all()

    @staticmethod
    def get_by_id(id):
        return Turma.query.get(id)

    @staticmethod
    def create(**kwargs):
        t = Turma(**kwargs)
        db.session.add(t)
        db.session.commit()
        return t

    @staticmethod
    def update(turma, **kwargs):
        for key, value in kwargs.items():
            setattr(turma, key, value)
        db.session.commit()
        return turma

    @staticmethod
    def delete(turma):
        db.session.delete(turma)
        db.session.commit()


# ---------- ALUNO ----------
class AlunoRepository:
    @staticmethod
    def get_all():
        return Aluno.query.all()

    @staticmethod
    def get_by_id(id):
        return Aluno.query.get(id)

    @staticmethod
    def create(**kwargs):
        a = Aluno(**kwargs)
        db.session.add(a)
        db.session.commit()
        return a

    @staticmethod
    def update(aluno, **kwargs):
        for key, value in kwargs.items():
            setattr(aluno, key, value)
        db.session.commit()
        return aluno

    @staticmethod
    def delete(aluno):
        db.session.delete(aluno)
        db.session.commit()
