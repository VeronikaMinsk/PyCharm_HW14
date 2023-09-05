import pytest

from Sem_6 import UserWorkshop, ErrorAccept, ErrorLevel, Person

@pytest.fixture
def user_workshop():
    return UserWorkshop('Ivanov', '2')

def test_login_successful(user_workshop):
    assert user_workshop.login('Petrov', '3') == '3'


def test_login_nonexistent_user(user_workshop):
    with pytest.raises(ErrorAccept):
        user_workshop.login('NonExistent', '100')

def test_create_user_successful(user_workshop):
    new_user = user_workshop.create_user('Unique_user', '10', '1')
    assert new_user is not None


def test_create_user_insufficient_level(user_workshop):
    with pytest.raises(ErrorLevel):
        user_workshop.create_user('New_user_3', '3', '5')


def test_create_user_existing_user(user_workshop):
    new_user = user_workshop.create_user('New_User_1', '4', '2')
    assert new_user is not None



def test_load_users():
    user_workshop = UserWorkshop('Ivanov', '2')
    assert len(UserWorkshop.user_list) > 0

def test_load_users_file_not_found(capfd):
    with pytest.raises(SystemExit):
        UserWorkshop.load_users('nonexistent.json')
    out, _ = capfd.readouterr()
    assert "Файл nonexistent.json не найден." in out

def test_person_object_creation():
    person = Person('Alice', '10', '3')
    assert person.name == 'Alice'
    assert person.id == '10'
    assert person.level == '3'
