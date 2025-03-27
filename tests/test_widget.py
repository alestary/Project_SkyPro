import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Счет 1222222234565433") == "**5433"
    assert mask_account_card("Visa Platinum 1222222234565433") == "1222 22** **** 5433"
    assert mask_account_card("Maestro 1222222234565433") == "1222 22** **** 5433"


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # Пустая строка
        None,  # None
        "abcdef",  # Не цифры
        "1234",  # Слишком короткая строка
        "123456789012345",  # 15 символов (не 16)
        "12345678901234567"  # 17 символов (не 16)
        "Visa Platinum 12222222345433",
        "Maestro 12222222345433",
        "Счет 321",
        "Maestro wwww",
    ],
)
def test_mask_account_card_invalid(invalid_input: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)


def test_valid_date() -> None:
    """Тест на корректное преобразование даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2000-01-01T00:00:00.000000") == "01.01.2000"
    assert get_date("1999-12-31T23:59:59.999999") == "31.12.1999"


@pytest.mark.parametrize(
    "invalid_date",
    [
        "",  # Пустая строка
        None,  # None
        "2024-03-11",  # Нет времени и миллисекунд
        "11.03.2024",  # Неверный формат
        "2024-02-30T12:00:00.000000",  # Несуществующая дата (30 февраля)
        "abcd-ef-ghTxx:yy:zz.ssssss",  # Полностью неверный формат
    ],
)
def test_invalid_dates(invalid_date: str) -> None:
    """Тест на обработку некорректных входных данных"""
    with pytest.raises(ValueError):
        get_date(invalid_date)
