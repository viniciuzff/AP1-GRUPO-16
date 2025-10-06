from app import app, db
from models import Professor, Turma, Aluno

with app.app_context():
    # 🔄 Recria o banco do zero
    db.drop_all()
    db.create_all()
    print("✅ Banco criado com sucesso!")

    # 👩‍🏫 Professores
    p1 = Professor(nome="Maria Oliveira", email="maria@escola.com", materia="Matemática", idade=35)
    p2 = Professor(nome="João Santos", email="joao@escola.com", materia="História", idade=42)
    db.session.add_all([p1, p2])
    db.session.commit()
    print("✅ Professores inseridos!")

    # 🏫 Turmas
    t1 = Turma(nome="Turma A - Manhã", professor_id=p1.id)
    t2 = Turma(nome="Turma B - Tarde", professor_id=p2.id)
    db.session.add_all([t1, t2])
    db.session.commit()
    print("✅ Turmas inseridas!")

    # 👨‍🎓 Alunos
    a1 = Aluno(nome="Ana Costa", idade=15, turma_id=t1.id, nota_primeiro_semestre=8.5, nota_segundo_semestre=9.0)
    a2 = Aluno(nome="Pedro Lima", idade=16, turma_id=t2.id, nota_primeiro_semestre=7.0, nota_segundo_semestre=8.0)
    a3 = Aluno(nome="Beatriz Souza", idade=15, turma_id=t1.id, nota_primeiro_semestre=9.0, nota_segundo_semestre=9.5)
    db.session.add_all([a1, a2, a3])
    db.session.commit()
    print("✅ Alunos inseridos!")

    # 📋 Exibe tudo no terminal
    print("\n📚 Dados no banco:")
    print("Professores:", Professor.query.all())
    print("Turmas:", Turma.query.all())
    print("Alunos:", Aluno.query.all())
