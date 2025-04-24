import json
import logging
import re
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("./logs/utils.log", encoding="utf-8")

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_data(path) -> Optional[list[dict]]:
    """
    Загружает данные из JSON-файла и возвращает их в виде списка
    """
    try:
        with open(path, encoding="utf-8") as f:
            logger.info("Загружает данные из JSON-файла и выводит в виде списка")
            data = json.load(f)
        if data:
            logger.info("Выводит JSON-файл")
            return data
        else:
            logger.debug("Выводит пустой список")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден")
        return []


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует список транзакций по строке поиска в описании с использованием регулярных выражений.
    Args:
        transactions (List[Dict]): Список словарей с данными о транзакциях.
        search_string (str): Строка для поиска в описании.
    Returns:
        List[Dict]: Отфильтрованный список транзакций, где в описании есть совпадение.
    """
    logger.info(f"Фильтрация транзакций по описанию с поисковой строкой: {search_string}")
    if not search_string:
        logger.info("Поисковая строка пуста, возвращаем исходный список транзакций")
        return transactions

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    filtered_transactions = []
    for transaction in transactions:
        if "description" not in transaction:
            logger.debug(f"Транзакция {transaction.get('id', 'без ID')} пропущена: отсутствует поле 'description'")
            continue
        if pattern.search(transaction["description"]):
            filtered_transactions.append(transaction)
            logger.debug(f"Транзакция {transaction.get('id', 'без ID')} соответствует поисковой строке")

    logger.info(f"Найдено {len(filtered_transactions)} транзакций, соответствующих поисковой строке")
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по заданным категориям.
    Args:
        transactions (List[Dict]): Список словарей с данными о транзакциях.
        categories (List[str]): Список категорий для подсчёта.
    Returns:
        Dict[str, int]: Словарь, где ключи — категории, а значения — количество операций.
    """
    logger.info("Подсчёт транзакций по категориям")
    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        if "description" not in transaction:
            logger.debug(f"Транзакция {transaction.get('id', 'без ID')} пропущена: отсутствует поле 'description'")
            continue
        description = transaction["description"]
        for category in categories:
            if category.lower() in description.lower():
                category_counts[category] += 1
                logger.debug(f"Транзакция {transaction.get('id', 'без ID')} отнесена к категории {category}")
                break

    logger.info(f"Результат подсчёта по категориям: {category_counts}")
    return category_counts

