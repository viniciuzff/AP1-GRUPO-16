from flask_restx import Namespace, Resource, fields
from flask import request
from app import db
from models import Professor

ns = Namespace('professores', description='Operações com professores')

prof_model = ns.model('Professor', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True),
    'email': fields.String,
    'materia': fields.String,
    'idade': fields.Integer,
})

@ns.route('/')
class ProfessorList(Resource):
    @ns.marshal_list_with(prof_model)
    def get(self):
        return Professor.query.all()

    @ns.expect(prof_model, validate=True)
    @ns.marshal_with(prof_model, code=201)
    def post(self):
        data = request.json
        p = Professor(nome=data.get('nome'), email=data.get('email'), materia=data.get('materia'), idade=data.get('idade'))
        db.session.add(p)
        db.session.commit()
        return p, 201

@ns.route('/<int:id>')
@ns.param('id', 'Identificador do professor')
class ProfessorItem(Resource):
    @ns.marshal_with(prof_model)
    def get(self, id):
        p = Professor.query.get_or_404(id)
        return p

    @ns.expect(prof_model, validate=True)
    @ns.marshal_with(prof_model)
    def put(self, id):
        p = Professor.query.get_or_404(id)
        data = request.json
        p.nome = data.get('nome', p.nome)
        p.email = data.get('email', p.email)
        p.materia = data.get('materia', p.materia)
        p.idade = data.get('idade', p.idade)
        db.session.commit()
        return p

    def delete(self, id):
        p = Professor.query.get_or_404(id)
        db.session.delete(p)
        db.session.commit()
        return '', 204
