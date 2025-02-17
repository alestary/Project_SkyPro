import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("1234567891011223") == "1234 56** **** 1223"


@pytest.mark.parametrize("invalid_input", [
    "",  # Пустая строка
    None,  # None
    "abcdef",  # Не цифры
    "1234",  # Слишком короткая строка
    "123456789012345",  # 15 символов (не 16)
    "12345678901234567"  # 17 символов (не 16)
])
def test_invalid_card_number(invalid_input):
    """Тест на некорректные входные данные"""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)


def test_get_mask_account():
    assert get_mask_account("1234567891011223") == "**1223"


@pytest.mark.parametrize("invalid_input", [
    "",  # Пустая строка
    None,  # None
    "abcdef",  # Не цифры
    "1234",  # Слишком короткая строка
    "123456789012345",  # 15 символов (не 16)
    "12345678901234567"  # 17 символов (не 16)
])
def test_invalid_mask_account(invalid_input):
    with pytest.raises(ValueError):
        get_mask_account(invalid_input)

