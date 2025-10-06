from flask_restx import Namespace, Resource, fields
from flask import request
from repositories import TurmaRepository, ProfessorRepository
from models import Turma

ns = Namespace('turmas', description='Operações com turmas')

turma_model = ns.model('Turma', {
    'id': fields.Integer(readonly=True),
    'descricao': fields.String(required=True),
    'professor_id': fields.Integer(required=True),
    'ativo': fields.Boolean,
})

@ns.route('/')
class TurmaList(Resource):
    @ns.marshal_list_with(turma_model)
    def get(self):
        return TurmaRepository.get_all()

    @ns.expect(turma_model, validate=True)
    @ns.marshal_with(turma_model, code=201)
    def post(self):
        payload = request.json
        # valida se o professor existe
        if not ProfessorRepository.get_by_id(payload.get('professor_id')):
            ns.abort(400, 'Professor não encontrado')
        t = TurmaRepository.create(**payload)
        return t, 201


@ns.route('/<int:id>')
@ns.param('id', 'Identificador da turma')
class TurmaItem(Resource):
    @ns.marshal_with(turma_model)
    def get(self, id):
        t = TurmaRepository.get_by_id(id)
        if not t:
            ns.abort(404)
        return t

    @ns.expect(turma_model, validate=True)
    @ns.marshal_with(turma_model)
    def put(self, id):
        t = TurmaRepository.get_by_id(id)
        if not t:
            ns.abort(404)
        payload = request.json
        if 'professor_id' in payload and not ProfessorRepository.get_by_id(payload.get('professor_id')):
            ns.abort(400, 'Professor não encontrado')
        t = TurmaRepository.update(t, **payload)
        return t

    def delete(self, id):
        t = TurmaRepository.get_by_id(id)
        if not t:
            ns.abort(404)
        TurmaRepository.delete(t)
        return '', 204
