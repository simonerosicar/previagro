from werkzeug.security import check_password_hash, generate_password_hash

from app.repositories.user_repository import UserRepository
from app.utils.exceptions import ValidationError


def create_user(username, password):
    if UserRepository.get_by_username(username) is not None:
        raise ValidationError("Nome de usuário já existe")

    password_hash = generate_password_hash(password)
    return UserRepository.create(username=username, password_hash=password_hash)


def authenticate_user(username, password):
    user = UserRepository.get_by_username(username)
    if user is None:
        return None

    if check_password_hash(user.password_hash, password):
        return user

    return None
