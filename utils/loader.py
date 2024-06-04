import json


def get_list_from_json_file(file_path) -> list:
    """
    читаем json файл и возвращаем список объектов
    :param file_path
    :return list
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
