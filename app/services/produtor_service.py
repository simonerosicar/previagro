from app.repositories.produtor_repository import ProdutorRepository
from app.utils.exceptions import ValidationError


def listar_produtores():
    return ProdutorRepository.all()


def criar_produtor(nome, cidade):
    return ProdutorRepository.create(nome=nome, cidade=cidade)


def get_produtor_or_404(produtor_id):
    return ProdutorRepository.get_or_404(produtor_id)


def atualizar_produtor(produtor, nome=None, cidade=None, ativo=None, partial=False):
    if not partial:
        if nome is None or cidade is None:
            raise ValidationError("Nome e cidade são obrigatórios")

    return ProdutorRepository.update(produtor, nome=nome, cidade=cidade, ativo=ativo)


def remover_produtor(produtor):
    return ProdutorRepository.delete(produtor)
