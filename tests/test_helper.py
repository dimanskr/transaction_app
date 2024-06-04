import pytest
from models.operation import Operation
from utils.helper import get_operations_by_status, get_last_operations


@pytest.fixture
def operations_data():
    return [
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2024-05-26T10:50:50.294041",
            "operationAmount": {
                "amount": "354321.44",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 223456789,
            "state": "CANCELED",
            "date": "2024-05-27T10:50:50.294041",
            "operationAmount": {
                "amount": "354322.44",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 323456789,
            "state": "EXECUTED",
            "date": "2024-05-28T10:50:50.294041",
            "operationAmount": {
                "amount": "54321.44",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 423456789,
            "state": "PENDING",
            "date": "2024-05-29T10:50:50.294041",
            "operationAmount": {
                "amount": "354321.44",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]


def test_get_operations_by_status(operations_data):
    operations = operations_data
    executed_operations = get_operations_by_status(operations, "EXECUTED")

    assert len(executed_operations) == 2
    assert all(op.state == "EXECUTED" for op in executed_operations)

    pending_operations = get_operations_by_status(operations, "PENDING")

    assert len(pending_operations) == 1
    assert all(op.state == "PENDING" for op in pending_operations)


def test_get_last_operations(operations_data):
    operations = [Operation(op) for op in operations_data]
    last_operations = get_last_operations(operations, 2)

    assert len(last_operations) == 2
    assert last_operations[0].date > last_operations[1].date

    all_sorted_operations = get_last_operations(operations, len(operations))

    for i in range(len(all_sorted_operations) - 1):
        assert all_sorted_operations[i].date >= all_sorted_operations[i + 1].date


if __name__ == "__main__":
    pytest.main()
