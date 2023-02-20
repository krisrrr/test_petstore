from requests import Response

from api.petstore_requests import PetStoreRequest


class Store(PetStoreRequest):
    """Класс для отправки запросов на группу методов /store"""

    def __init__(self):
        super().__init__()
        self.url = self.url.format(path='/store{path}')

    def create_order(self, json: dict, path: str = '/order') -> Response:
        """Создать заказ на питомца

        Args:
            json: тело запроса
            path: метод сервиса
        """
        return self.request(method='POST', url=self.url.format(path=path), json=json)

    def find_order_by_id(self, order_id: str, path: str = '/order/{order_id}') -> Response:
        """Найти заказ по его id

        Args:
            order_id: id заказа
            path: метод сервиса
        """
        return self.request(url=self.url.format(path=path.format(order_id=order_id)))
