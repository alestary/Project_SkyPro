def filter_by_state(data_list, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_list: Список словарей.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data_list if item.get('state') == state]

from datetime import datetime

def sort_by_date(data_list, descending=True):
    """
    Сортирует список словарей по дате.

    :param data_list: Список словарей.
    :param descending: Порядок сортировки (True для убывания, False для возрастания).
    :return: Отсортированный список словарей.
    """
    return sorted(
        data_list,
        key=lambda x: datetime.strptime(x.get('date', '0001-01-01'), '%Y-%m-%d'),
        reverse=descending
    )
