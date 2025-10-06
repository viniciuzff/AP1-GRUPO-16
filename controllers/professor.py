from flask_restx import Namespace, Resource, fields
from flask import request
from repositories import ProfessorRepository
from models import Professor

ns = Namespace('professores', description='Operações com professores')

prof_model = ns.model('Professor', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'email': fields.String(required=True),
    'disciplina': fields.String,
    'ativo': fields.Boolean
})

@ns.route('/')
class ProfessorList(Resource):
    @ns.marshal_list_with(prof_model)
    def get(self):
        """Listar todos os professores"""
        return ProfessorRepository.get_all()

    @ns.expect(prof_model, validate=True)
    @ns.marshal_with(prof_model, code=201)
    def post(self):
        """Cadastrar um novo professor"""
        payload = request.json
        novo = ProfessorRepository.create(**payload)
        return novo, 201


@ns.route('/<int:id>')
@ns.param('id', 'Identificador do professor')
class ProfessorItem(Resource):
    @ns.marshal_with(prof_model)
    def get(self, id):
        """Obter um professor pelo ID"""
        prof = ProfessorRepository.get_by_id(id)
        if not prof:
            ns.abort(404)
        return prof

    @ns.expect(prof_model, validate=True)
    @ns.marshal_with(prof_model)
    def put(self, id):
        """Atualizar um professor"""
        prof = ProfessorRepository.get_by_id(id)
        if not prof:
            ns.abort(404)
        payload = request.json
        atualizado = ProfessorRepository.update(prof, **payload)
        return atualizado

    def delete(self, id):
        """Excluir um professor"""
        prof = ProfessorRepository.get_by_id(id)
        if not prof:
            ns.abort(404)
        ProfessorRepository.delete(prof)
        return '', 204
