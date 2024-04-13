from models.user import User
from database import Database
import pytest

db = Database()

@pytest.fixture
def empty_user():
    """Returns an empty user instance"""
    return User(database=None)

@pytest.fixture
def user():
    """Returns a user instance"""
    user = User(db)

    status = user.login("test@test.cl", "test")

    if not status:
        user.register("test", "test@test.cl", "test")

    return user