# Задание №5
#   Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# - Загрузка данных (функция из задания 4)
# - Вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# - Добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.
#   Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
#   Передавайте необходимые данные из основного кода
# проекта.


import json


class ErrorLevel(Exception):
    def __init__(self, current_level, required_level):
        self.current_level = current_level
        self.required_level = required_level

    def __str__(self):
        return f"Недостаточный уровень доступа. Текущий уровень: {self.current_level}, требуемый уровень: {self.required_level}"

class ErrorAccept(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Пользователь {self.name} не найден в базе данных"

class Person:
    def __init__(self, name, id, level=None):
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash((self.name, self.id))

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Level: {self.level}"

class UserWorkshop:
    user_list = set()

    def __init__(self, cur_name, cur_id):
        self.cur_name = cur_name
        self.cur_id = cur_id
        UserWorkshop.load_users()

    @staticmethod
    def load_users(path='test_bd.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(Person(name, str(id), str(level)))

    def login(self, name, id):
        login_user = Person(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:
                return user.level
        else:
            raise ErrorAccept(name)

    def create_user(self, name, id, level):
        if current_level := self.login(self.cur_name, self.cur_id):
            for user in UserWorkshop.user_list:
                if user.name == name and user.id == id:
                    raise ValueError(f"Пользователь с именем {name} и ID {id} уже существует")
            if int(current_level) > int(level):
                new_user = Person(name, id, level)
                UserWorkshop.user_list.add(new_user)
                return new_user
            else:
                raise ErrorLevel(current_level, level)

try:
    b = UserWorkshop('Ivanov', '2')
    print(b.login('Petrov', '3'))
    print(b.create_user('New_user', '1', '3'))    # Меняем уровень доступа
except ErrorAccept as e:
    print(f"Ошибка авторизации: {e}")
except ErrorLevel as e:
    print(f"Ошибка уровня доступа: {e}")

