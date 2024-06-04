from models.operation import Operation


def payment_details(payment_str: str | None) -> str | None:
    """
    Разбиваем детали платежа на название карты (счета) и номер, скрываем цифры номера с помощью функции 'mask_number'
    :param payment_str: str | None
    :return: str | None
    """
    # если есть название и номер карты, то разбиваем их
    if payment_str:
        parts = payment_str.split()
        name = ' '.join(parts[:-1])
        number = parts[-1]
        # если номер состоит из цифр и длинна 16 или 20 символов, возвращаем строку со спрятанной информацией
        if number.isdigit() and (len(number) in [16, 20]):
            return f"{name} {mask_number(number)}"

    return None


def mask_number(card_number: str) -> str:
    """
    Скрываем номер счета или карты по заданному условию
    :param card_number: string
    :return: masked string
    """
    # если 16 символов - номер карточки, если 20 - номер счета
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return f"**{card_number[-4:]}"


def output_operation_detail(operation: Operation) -> str:
    """
    Выводим информацию по платежу в указанном формате
    :param operation: Operation
    :return: str
    """
    if payment_details(operation.from_account):
        transfer_direction = f"{payment_details(operation.from_account)} -> {payment_details(operation.to_account)}"
    else:
        transfer_direction = f"{payment_details(operation.to_account)}"

    return (f"{operation.formated_date()} {operation.description}\n"
            f"{transfer_direction}\n"
            f"{operation.amount:.2f} {operation.currency_name}\n")
