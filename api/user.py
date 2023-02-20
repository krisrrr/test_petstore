from requests import Response

from api.petstore_requests import PetStoreRequest
from users import User


class UserApi(PetStoreRequest):
    """Класс для отправки запросов на группу методов /user"""

    def __init__(self):
        self.url = self.url.format(path='/user{path}')

    def new_user(self, json: dict, path: str = '') -> Response:
        """Создать нового пользователя/Зарегистрироваться

        Args:
            json: тело запроса
            path: метод сервиса
        """
        return self.request(method='POST', json=json, url=self.url.format(path=path))

    def login(self, user: User, path: str = '/login'):
        """Аутентифицироваться

        Args:
            user: пользователь
            path: метод сервиса
        """
        self.headers.update({
            'api_key': self.request(
                params={
                    'username': user.username,
                    'password': user.password
                },
                url=self.url.format(path=path)
            ).text
        })

    def logout(self, path: str = '/logout'):
        """Выйти из учетной записи

        Args:
            path: метод сервиса
        """
        self.request(url=self.url.format(path=path))
        self.headers.pop('api_key')
