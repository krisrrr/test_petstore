from requests import Response

from api.petstore_requests import PetStoreRequest


class Pet(PetStoreRequest):
    """Класс для отправки запросов на группу методов /pet"""

    def __init__(self):
        super().__init__()
        self.url = self.url.format(path='/pet{path}')

    def add(self, json: dict, path: str = '') -> Response:
        """ Добавить питомца

        Args:
            json: тело запроса
            path: метод сервиса
        """
        return self.request(method='POST', url=self.url.format(path=path), json=json)

    def delete(self, pet_id: int, path: str = '/{pet_id}') -> Response:
        """ Удалить питомца

        Args:
            pet_id: идентификатор питомца
            path: метод сервиса
        """
        return self.request(method='DELETE', url=self.url.format(path=path.format(pet_id=pet_id)))

    def find_pet_by_id(self, pet_id: int, path: str = '/{pet_id}') -> Response:
        """ Найт питомца по идентификатору

        Args:
            pet_id: идентификатор питомца
            path: метод сервиса
        """
        return self.request(url=self.url.format(path=path.format(pet_id=pet_id)))
