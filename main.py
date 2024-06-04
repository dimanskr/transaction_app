from settings import OPERATIONS_FILE
from utils.loader import get_list_from_json_file


def main():
    # список словарей из json файла
    operations_list = get_list_from_json_file(OPERATIONS_FILE)


if __name__ == '__main__':
    main()
