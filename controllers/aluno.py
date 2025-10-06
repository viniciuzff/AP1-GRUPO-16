from flask_restx import Namespace, Resource, fields
from flask import request
from repositories import AlunoRepository, TurmaRepository
from models import Aluno

ns = Namespace('alunos', description='Operações com alunos')

aluno_model = ns.model('Aluno', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'idade': fields.Integer,
    'turma_id': fields.Integer(required=True),
    'data_nascimento': fields.String,  # ISO date
    'nota_primeiro_semestre': fields.Float,
    'nota_segundo_semestre': fields.Float,
    'media_final': fields.Float,
})

@ns.route('/')
class AlunoList(Resource):
    @ns.marshal_list_with(aluno_model)
    def get(self):
        return AlunoRepository.get_all()

    @ns.expect(aluno_model, validate=True)
    @ns.marshal_with(aluno_model, code=201)
    def post(self):
        payload = request.json
        if not TurmaRepository.get_by_id(payload.get('turma_id')):
            ns.abort(400, 'Turma não encontrada')
        a = AlunoRepository.create(**payload)
        return a, 201