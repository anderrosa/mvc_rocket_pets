from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetRepository:
    def list_pets(self):
        return [
            PetsTable(id=4, name="Fluffy", type="cat"),
            PetsTable(id=47, name="Buddy", type="dog")
        ]
def test_list_pets():
    controller = PetListerController(MockPetRepository())
    response = controller.list()

    expected_response = {
        "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    {"id": 4, "name": "Fluffy"},
                    {"id": 47, "name": "Buddy"}
                ]
            }
    }

    assert response == expected_response
