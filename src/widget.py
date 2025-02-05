from datetime import datetime


def mask_account_card(name: str, number: str) -> str:
    if name.lower().startswith("счет"):
        """Маскировка счёта: оставляем только 4 последние цифры"""
        account_card = "**" + number[-4:]
    else:
        """Маскировка карты: 4 первых цифры, 2 открытые в середине, 4 последние"""
        account_card = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    return account_card


def get_date(date: str) -> str:
    """Переформатирование даты"""
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
