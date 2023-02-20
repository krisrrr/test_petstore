class User:
    """Класс тестового пользователя"""

    def __init__(self, username: str, password: str):
        """
        Args:
            username: логин
            password: пароль
        """
        self.username = username
        self.password = password


USER_1 = User(username='', password='')
