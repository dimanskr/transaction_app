from settings import OPERATIONS_FILE, OPERATIONS_COUNT
from utils.helper import get_operations_by_status, get_last_operations
from utils.loader import get_list_from_json_file


def main():
    # список словарей из json файла
    operations_list = get_list_from_json_file(OPERATIONS_FILE)
    # список операций согласно статусу
    operations = get_operations_by_status(operations_list, status="EXECUTED")
    # список последних операций
    last_operations = get_last_operations(operations, OPERATIONS_COUNT)


if __name__ == '__main__':
    main()
