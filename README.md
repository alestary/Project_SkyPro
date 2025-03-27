 # Проект "Фича для личного кабинета клиента банка"

## Описание:

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Проект, который будет готовить данные для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/alestary/Project_SkyPro
```

2. Перейдите в директорию проекта:
```
cd Project_SkyPro
```

3. Создайте виртуальное окружение (опционально):
```
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows
```

4. Установите зависимости (если они есть):
```
pip install -r requirements.txt
```
## Использование
Фильтрация данных
Функция filter_by_state позволяет отфильтровать список словарей по значению ключа state.

```from src.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

filtered_data = filter_by_state(data, state='EXECUTED')
print(filtered_data) 
```
### Результат 
```[
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]
```
## Сортировка данных
Функция sort_by_date сортирует список словарей по дате (date). Порядок сортировки можно задать через параметр descending.

```from src.processing import sort_by_date

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

sorted_data = sort_by_date(data, descending=False)
print(sorted_data)
```
### Результат:
```[
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]
```
## Фильтер
Функция filter_by_currency принимает на вход список словарей, представляющих транзакции.
Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).

``` 
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions)) 
```
### Результат
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
## Описание транзакций
Генератор transaction_description принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```
### Результат
```
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
## Генератор номеров банковских карт
Генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты. 
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.

```
for card_number in card_number_generator(1, 5):
    print(card_number)
```
```
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
## Тестирование
Также к каждой функции прописаны тестирования. Тестирование кода играет важную роль в разработке программного обеспечения. 
Оно не просто помогает обнаруживать ошибки и проблемы в коде до того, как продукт будет выпущен, 
но также способствует высокому качеству и надежности программных решений.

Автор : alestary
GitHub : https://github.com/alestary
