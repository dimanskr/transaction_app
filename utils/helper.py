from models.operation import Operation


def get_operations_by_status(status: str, *operations_list: dict) -> list[Operation]:
    """
    Получаем список объектов из списка операций согласно статусу
    :param operations_list: list[dict]
    :param status: str
    :return: list[Operation]
    """
    return [
        Operation(op)
        for op in operations_list
        if op and op.get("state") == status
    ]


def get_last_operations(operations_count: int, *operations: Operation) -> list[Operation]:
    """
    Сортируем операции по дате и выводим последние 'operations_count' операций
    :param operations: list[Operation]
    :param operations_count: int
    :return: list[Operation]
    """
    sorted_operations = sorted(operations, key=lambda op: op.date, reverse=True)
    return sorted_operations[:operations_count]
