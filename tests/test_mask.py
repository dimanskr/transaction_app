import pytest
from models.operation import Operation
from views.mask import payment_details, output_operation_detail, mask_card_number, mask_account_number


def test_payment_details():
    assert payment_details("Master Card 1234567812345678") == "Master Card 1234 56** **** 5678"
    assert payment_details("Счет 12345678901234567890") == "Счет **7890"
    assert payment_details(None) is None
    assert payment_details("InvalidData") is None
    assert payment_details("Invalid Data") is None
    assert payment_details("MasterCard 1234abcd5678efgh") is None
    assert payment_details("MasterCard 1234567890123456789") is None
    assert payment_details("MasterCard 1234567890123456789123456789") is None


def test_mask_card_number():
    assert mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_mask_account_number():
    assert mask_account_number("12345678901234567890") == "**7890"


def test_output_operation_detail():
    operations_data = [
        {
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
        },
        {
            "id": 223456789,
            "state": "EXECUTED",
            "date": "2024-05-06T10:50:58.294042",
            "operationAmount": {
                "amount": "4321.33",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779589"
        }
    ]
    first_operation = Operation(operations_data[0])
    second_operation = Operation(operations_data[1])

    first_expected_output = ("05.05.2024 Перевод с карты\n"
                             "Visa Premium 1596 83** **** 5199 -> Счет **9589\n"
                             "4321.33 руб.\n")

    second_expected_output = ("06.05.2024 Открытие вклада\n"
                              "Счет **9589\n"
                              "4321.33 руб.\n")

    assert output_operation_detail(first_operation) == first_expected_output
    assert output_operation_detail(second_operation) == second_expected_output


if __name__ == "__main__":
    pytest.main()
