from app import db
from app.models import Produtor
from werkzeug.exceptions import NotFound


class ProdutorRepository:
    @staticmethod
    def all():
        return Produtor.query.all()

    @staticmethod
    def get_or_404(produtor_id):
        produtor = db.session.get(Produtor, produtor_id)
        if produtor is None:
            raise NotFound()
        return produtor

    @staticmethod
    def create(nome, cidade, ativo=True):
        produtor = Produtor(nome=nome, cidade=cidade, ativo=ativo)
        db.session.add(produtor)
        db.session.commit()
        return produtor

    @staticmethod
    def update(produtor, nome=None, cidade=None, ativo=None):
        if nome is not None:
            produtor.nome = nome
        if cidade is not None:
            produtor.cidade = cidade
        if ativo is not None:
            produtor.ativo = ativo
        db.session.commit()
        return produtor

    @staticmethod
    def delete(produtor):
        db.session.delete(produtor)
        db.session.commit()
