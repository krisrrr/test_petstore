import pytest

from api.pet import Pet
from api.store import Store
from logger_ import logger
from users import USER_1

CODE_MESSAGE = 'Код статуса ответа отличен от 200'


class TestE2EWayOfPet:

    @staticmethod
    @pytest.mark.parametrize('auth', [USER_1], indirect=True)
    def test_e2e_way_of_pet(auth):
        store_api = Store()
        pet_api = Pet()

        logger.log('Создать заказ на питомца')
        request_json = {
            "id": 0,
            "petId": 0,
            "quantity": 0,
            "shipDate": "2023-02-20T14:59:07.726Z",
            "status": "placed",
            "complete": False
        }
        response = store_api.create_order(json=request_json)

        assert response.status_code == 200, CODE_MESSAGE
        content = response.json()
        assert content == request_json

        logger.log('Получить заказ по ID')
        order_id = content['id']
        response = store_api.find_order_by_id(order_id=order_id)
        assert response.status_code == 200, CODE_MESSAGE
        body = response.json()
        assert body == request_json

        pet_id = body['petId']

        logger.log('Добавить питомца')
        request_json = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "kQOcMTuJL9UapDxT2T7OUhTxSGejMVpoaUTfoaeIfsfivi9ABFhvGRdJTHMeuDivYRXXDL9.SaaNJIf0NEexnHd3qxcMgR"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ]
        }
        response = pet_api.add(json=request_json)
        assert response.status_code == 200, CODE_MESSAGE
        content = response.json()
        assert content == request_json

        logger.log('Удалить питомца')
        assert pet_api.delete(pet_id=pet_id).status_code == 200, CODE_MESSAGE
