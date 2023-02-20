from requests import Request, Response, request

from logger_ import log_request, log_response


class PetStoreRequest:
    """Бвзовый класс для отправки запросов"""

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    url = 'http://petstore.swagger.io/v2{path}'
    params: dict = None
    data: dict = None
    json: dict = None

    def request(self, url: str = None, method: str = 'get', headers: dict = None, data: dict or list = None,
                params: dict = None,  json: dict = None) -> Response:
        """Отправить запрос

        Args:
            url: URL запроса
            method: HTTP-метод
            headers: заголовки запроса
            json: тело запроса в формате JSON
            data: тело запроса в формате отличном о JSON
            params: параметры запроса
        """
        log_request(
            request=Request(
                url=url if url else self.url,
                method=method,
                headers=headers if headers else self.headers,
                params=params if params else self.params,
                data=data if data else self.data,
                json=json if json else self.json
            ).prepare()
        )
        response = request(
            url=url if url else self.url,
            method=method,
            headers=headers if headers else self.headers,
            params=params if params else self.params,
            data=data if data else self.data,
            json=json if json else self.json,
            verify=False,
        )
        log_response(response=response)
        return response
