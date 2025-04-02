import json
from unittest.mock import mock_open, patch

from src.utils import get_data


def test_get_data() -> None:
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, "description": '
        '"Перевод организации", '
        '"from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]'
    )
    mock_file = mock_open(read_data=mock_data)

    with patch("builtins.open", mock_file):
        result = get_data("../data/operations.json")

    expected_result = json.loads(mock_data)

    assert result == expected_result
    mock_file.assert_called_once()
