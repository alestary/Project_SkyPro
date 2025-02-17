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
## Тестирование
Также к каждой функции прописаны тестирования. Тестирование кода играет важную роль в разработке программного обеспечения. Оно не просто помогает обнаруживать ошибки и проблемы в коде до того, как продукт будет выпущен, но также способствует высокому качеству и надежности программных решений.

Автор : alestary
GitHub : https://github.com/alestary
