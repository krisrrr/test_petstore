import pytest as pytest
from _pytest.fixtures import SubRequest

from api.pet import Pet
from api.user import UserApi
from logger_ import logger


@pytest.fixture(scope='function')
def auth(request: SubRequest):
    logger.log(f'Фикстура. Аутентифицироваться под пользователем с логином {request.param.login}')
    auth_api = UserApi()
    auth_api.login(user=request.param)

    yield

    logger.log("Разлогиниться")
    auth_api.logout()


@pytest.fixture(scope='class')
def create_and_delete_pet(request: SubRequest):
    logger.log("Фикстура. Создать питомца")
    category = request.param[0]
    name = request.param[1]
    tag = request.param[2]

    pet_api = Pet()

    response = pet_api.add(json={
        "id": 0,
        "category": {
            "id": 0,
            "name": category
        },
        "name": name,
        "photoUrls": ['empty'],
        "tags": [
            {
                "id": 0,
                "name": tag
            }
        ]
    })
    assert response.status_code == 200, 'Код ответа отличен от ожидаемого, не удалось создать питомца'
    id_ = response.json()['id']

    yield id_

    logger.log("Удалить питомца")
    assert pet_api.delete(pet_id=id_).status_code == 200, \
        'Код ответа отличен от ожидаемого, не удалось удалить питомца'
