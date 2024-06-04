from models.operation import Operation


def get_operations_by_status(operations_list: list[dict], status: str) -> list[Operation]:
    """
    Получаем список объектов из списка операций согласно статусу
    :param operations_list: list[dict]
    :param status: str
    :return: list[Operation]
    """
    return [Operation(op) for op in operations_list if op and op["state"] == status]


def get_last_operations(operations: list[Operation], operations_count: int) -> list[Operation]:
    """
    Сортируем операции по дате и выводим последние 'operations_count' операций
    :param operations: list[Operation]
    :param operations_count: int
    :return: list[Operation]
    """
    operations.sort(key=lambda op: op.date, reverse=True)
    return operations[:operations_count]
