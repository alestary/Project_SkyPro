from typing import Any


def log(filename: str = None):
    """Декоратор для логирования выполнения функций
    Логирует начало и конец выполнения функции, а также результаты или ошибки
    Логи могут быть записаны в файл или выведены в консоли"""

    def decorator(func: Any):
        """Внутренний декоратор, который применяется к функции"""

        def wrapper(*args: tuple, **kwargs: dict):
            """Обертка вокруг декорируемой функции
            Логирует успешное выполнение или ошибку функции, а также входные параметры"""
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(message)
                else:
                    print(message, end="")
            return result

        return wrapper

    return decorator
