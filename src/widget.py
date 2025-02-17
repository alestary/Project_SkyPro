from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

# def mask_account_card(name, number: str):
#     if name.lower().startswith("счет"):
#         """Маскировка счёта: оставляем только 4 последние цифры"""
#         account_card = "**" + number[-4:]
#     else:
#         """Маскировка карты: 4 первых цифры, 2 открытые в середине, 4 последние"""
#         account_card = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
#     return account_card


def mask_account_card(date: str) -> str:
    if date is None or date == "":
        raise ValueError("date cannot be None")

    separate_date = date.split()
    if separate_date[0] == "Счет":
        return get_mask_account(separate_date[1])

    elif separate_date[0] == "Visa" and separate_date[1] == "Platinum":
        return get_mask_card_number(separate_date[2])

    elif separate_date[0] == "Maestro":
        return get_mask_card_number(separate_date[1])

    else:
        raise ValueError("Uncorrected date format")


def get_date(date: str) -> str:
    """Переформатирование даты из ISO 8601 в формат ДД.ММ.ГГГГ."""
    if not isinstance(date, str) or not date.strip():
        raise ValueError("Некорректный ввод: дата отсутствует или имеет неверный формат")

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидался ISO 8601 (YYYY-MM-DDTHH:MM:SS.ssssss)")
