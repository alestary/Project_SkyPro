import json
from typing import Optional
import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")

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
