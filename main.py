class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self._access_level = access_level
        else:
            raise ValueError("Access level must be either 'user' or 'admin'.")

    def __str__(self):
        return f"User[ID={self._user_id}, Name={self._name}, Access Level={self._access_level}]"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._admin_level = 'admin'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
        else:
            raise TypeError("Only User instances can be added.")

    def remove_user(self, user_list, user_id):
        user_to_remove = None
        for user in user_list:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break

        if user_to_remove:
            user_list.remove(user_to_remove)
        else:
            raise ValueError("User with the given ID not found.")

    def __str__(self):
        return f"Admin[ID={self._user_id}, Name={self._name}, Access Level={self._admin_level}]"

# Пример использования
if __name__ == "__main__":
    # Создаем список пользователей
    user_list = []

    # Создаем обычного пользователя
    user1 = User(user_id=1, name="Alice")

    # Создаем администратора
    admin1 = Admin(user_id=2, name="Bob")

    # Добавляем пользователя через администратора
    admin1.add_user(user_list, user1)

    # Проверяем список пользователей
    for user in user_list:
        print(user)

    # Удаляем пользователя через администратора
    admin1.remove_user(user_list, user_id=1)

    # Проверяем список пользователей после удаления

    for user in user_list:
        print(user)