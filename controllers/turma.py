from flask_restx import Namespace, Resource, fields
from flask import request
from app import db
from models import Turma, Professor

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
        return Turma.query.all()

    @ns.expect(turma_model, validate=True)
    @ns.marshal_with(turma_model, code=201)
    def post(self):
        data = request.json
        # valida professor existe
        if not Professor.query.get(data.get('professor_id')):
            ns.abort(400, 'Professor não encontrado')
        t = Turma(descricao=data.get('descricao'), professor_id=data.get('professor_id'), ativo=data.get('ativo', True))
        db.session.add(t)
        db.session.commit()
        return t, 201

@ns.route('/<int:id>')
@ns.param('id', 'Identificador da turma')
class TurmaItem(Resource):
    @ns.marshal_with(turma_model)
    def get(self, id):
        t = Turma.query.get_or_404(id)
        return t

    @ns.expect(turma_model, validate=True)
    @ns.marshal_with(turma_model)
    def put(self, id):
        t = Turma.query.get_or_404(id)
        data = request.json
        if 'professor_id' in data and not Professor.query.get(data.get('professor_id')):
            ns.abort(400, 'Professor não encontrado')
        t.descricao = data.get('descricao', t.descricao)
        t.professor_id = data.get('professor_id', t.professor_id)
        t.ativo = data.get('ativo', t.ativo)
        db.session.commit()
        return t

    def delete(self, id):
        t = Turma.query.get_or_404(id)
        db.session.delete(t)
        db.session.commit()
        return '', 204
