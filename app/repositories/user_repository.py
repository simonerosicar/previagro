from app import db
from app.models import User
from werkzeug.exceptions import NotFound


class UserRepository:
    @staticmethod
    def all():
        return User.query.all()

    @staticmethod
    def get_or_404(user_id):
        user = db.session.get(User, user_id)
        if user is None:
            raise NotFound()
        return user

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create(username, password_hash):
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user
