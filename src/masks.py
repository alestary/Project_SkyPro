import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера."""

    if not isinstance(card_number, str) or not card_number.isdigit():
        logger.error("Пользователь ввел неккоректные данные")
        raise ValueError("Некорректный ввод: номер карты должен быть строкой из цифр")

    if len(card_number) == 16:
        logger.debug("Карта соответсвует")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Пользовтель ввел некорректный номер карты")
        raise ValueError("Некорректный номер карты: ожидалось 16 цифр")


def get_mask_account(account_number: str) -> str:

    if not isinstance(account_number, str) or not account_number.isdigit():
        logger.error("Пользователь ввел некорректные данные")
        raise ValueError("Некорректный ввод: номер карты должен быть строкой из цифр")

    if len(account_number) == 16:
        logger.debug("Карта соответствует")
        masked_account_number = f"**{account_number[-4:]}"
        return masked_account_number
    else:
        logger.error("Пользовтель ввел некорректный номер карты")
        raise ValueError("Некорректный номер карты: ожидалось 16 цифр")
