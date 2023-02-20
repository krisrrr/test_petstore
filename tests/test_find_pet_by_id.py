import pytest

from api.pet import Pet
from logger_ import logger
from users import USER_1


class TestFindPetByID:

    @staticmethod
    @pytest.mark.parametrize('auth', [USER_1], indirect=True)
    def test_find_pet_by_id(crete_and_delete_pet, auth):
        pet_id = crete_and_delete_pet
        logger.log("Найти питомца по ID")
        response = Pet().find_pet_by_id(pet_id=pet_id)

        assert response.status_code == 200, 'Код статуса ответа отличен от 200'
        assert response.json()['id'] == pet_id
