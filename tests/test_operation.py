import pytest
from datetime import datetime
from models.operation import Operation


@pytest.fixture
def operation_data():
    return {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2024-05-05T10:50:58.294042",
        "operationAmount": {
            "amount": "4321.33",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты",
        "from": "Visa Premium 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_operation_init(operation_data):
    operation = Operation(operation_data)

    assert operation.id == 123456789
    assert operation.state == "EXECUTED"
    assert operation.date == datetime.strptime("2024-05-05T10:50:58.294042", "%Y-%m-%dT%H:%M:%S.%f")
    assert operation.amount == 4321.33
    assert operation.currency_name == "руб."
    assert operation.currency_code == "RUB"
    assert operation.description == "Перевод с карты"
    assert operation.from_account == "Visa Premium 1596837868705199"
    assert operation.to_account == "Счет 64686473678894779589"


def test_formatted_date(operation_data):
    operation = Operation(operation_data)
    assert operation.formated_date() == "05.05.2024"


if __name__ == "__main__":
    pytest.main()
