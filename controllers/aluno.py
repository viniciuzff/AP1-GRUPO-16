from flask_restx import Namespace, Resource, fields
from flask import request
from app import db
from models import Aluno, Turma

ns = Namespace('alunos', description='Operações com alunos')

aluno_model = ns.model('Aluno', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'idade': fields.Integer,
    'turma_id': fields.Integer(required=True),
    'data_nascimento': fields.String,
    'nota_primeiro_semestre': fields.Float,
    'nota_segundo_semestre': fields.Float,
    'media_final': fields.Float,
})

@ns.route('/')
class AlunoList(Resource):
    @ns.marshal_list_with(aluno_model)
    def get(self):
        return Aluno.query.all()

    @ns.expect(aluno_model, validate=True)
    @ns.marshal_with(aluno_model, code=201)
    def post(self):
        data = request.json
        if not Turma.query.get(data.get('turma_id')):
            ns.abort(400, 'Turma não encontrada')
        a = Aluno(
            nome=data.get('nome'),
            idade=data.get('idade'),
            turma_id=data.get('turma_id'),
            data_nascimento=data.get('data_nascimento'),
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final')
        )
        db.session.add(a)
        db.session.commit()
        return a, 201

@ns.route('/<int:id>')
@ns.param('id', 'Identificador do aluno')
class AlunoItem(Resource):
    @ns.marshal_with(aluno_model)
    def get(self, id):
        a = Aluno.query.get_or_404(id)
        return a

    @ns.expect(aluno_model, validate=True)
    @ns.marshal_with(aluno_model)
    def put(self, id):
        a = Aluno.query.get_or_404(id)
        data = request.json
        if 'turma_id' in data and not Turma.query.get(data.get('turma_id')):
            ns.abort(400, 'Turma não encontrada')
        a.nome = data.get('nome', a.nome)
        a.idade = data.get('idade', a.idade)
        a.turma_id = data.get('turma_id', a.turma_id)
        a.data_nascimento = data.get('data_nascimento', a.data_nascimento)
        a.nota_primeiro_semestre = data.get('nota_primeiro_semestre', a.nota_primeiro_semestre)
        a.nota_segundo_semestre = data.get('nota_segundo_semestre', a.nota_segundo_semestre)
        a.media_final = data.get('media_final', a.media_final)
        db.session.commit()
        return a

    def delete(self, id):
        a = Aluno.query.get_or_404(id)
        db.session.delete(a)
        db.session.commit()
        return '', 204
