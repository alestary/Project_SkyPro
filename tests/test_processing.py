from typing import List

import pytest

from src.processing import filter_by_state
from tests.confest import test_data


@pytest.mark.parametrize(
    "state, expected_result",
    [
        (
            "EXECUTED",
            [  # Ожидаем только 'EXECUTED'
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [  # Ожидаем только 'CANCELED'
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PENDING", []),  # Нет записей со статусом 'PENDING'
        ("", []),  # Пустой статус — тоже ничего
        (None, []),  # None как статус — ничего не должно вернуться
    ],
)
def test_filter_by_state(state: str, expected_result: List, test_data: List) -> None:
    """Параметризованный тест фильтрации по статусу"""
    assert filter_by_state(test_data, state) == expected_result


def test_empty_list() -> None:
    """Тест на случай, если входной список пуст"""
    assert filter_by_state([]) == []


def test_default_state(test_data: List) -> None:
    """Тест на фильтрацию по умолчанию (EXECUTED)"""
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(test_data) == expected
