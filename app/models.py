from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "ativo": self.ativo,
        }


class Produtor(db.Model):

    __tablename__ = "produtores"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    cidade = db.Column(
        db.String(100),
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cidade": self.cidade,
            "ativo": self.ativo,
        }
    