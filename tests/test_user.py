from fixtures import user
from fixtures import empty_user

def test_empty_user(empty_user: empty_user):
    """
    Test if the empty user has the correct attributes.
    """
    assert empty_user.id == None
    assert empty_user.username == None
    assert empty_user.email == None

def test_user_register(user: user):
    """
    Test if the user is registered correctly.
    """
    assert user.id != None
    assert user.email == "test@test.cl"

def test_user_login(user: user):
    """
    Test if the user is logged in correctly.
    """
    assert user.login("test@test.cl", "test")

def test_keychain_user(user: user):
    """
    Test if the user has a keychain.
    """
    keychain = user.keychain
    assert keychain != None

def test_add_password(user: user):
    """
    Test if the password is added to the keychain.
    """
    keychain = user.keychain

    keychain.delete_password("test")
    keychain.add_password("test", "test")

    assert keychain.get_password("test") == "test"

def test_change_password(user: user):
    """
    Test if the password is changed in the keychain.
    """
    keychain = user.keychain

    keychain.delete_password("test")
    keychain.add_password("test", "test")
    keychain.change_password("test", "test2")

    assert keychain.get_password("test") == "test2"

def test_delete_password(user: user):
    """
    Test if the password is deleted from the keychain.
    """
    keychain = user.keychain

    keychain.delete_password("test")

    assert keychain.get_password("test") == None
