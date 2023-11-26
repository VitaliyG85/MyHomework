# def password_checker(func: callable([])) -> callable:
#     def wrapper(password):
#         if ((len(password) > 7)
#                 and (not (password.isalnum() or password.islower() or password.isupper() or password.isalpha()))):
#             return func(password)
#         else:
#             print('Ошибка, пароль не соответствует параметрам сложности')
#     return wrapper
#
#
# @password_checker
# def register_user(password: str) -> str:
#     return f'Пользователь зарегистрирован с паролем {password}'
#
#
# print(register_user('Rwrre$dfgdgfdg@'))

import csv


def username_validator(func: callable) -> callable:
    """
    Декоратор для валидации имени пользователя
    :param func:  функция для оборачивания
    :return: обернутая функция
    """

    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError('В имени пользователя не должно быть пробелов')
        return func(username, password)

    return wrapper


def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1,
                       min_special_chars: int = 1) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError(f'Пароль должен быть не короче {min_length} символов')
            flag_upper = False
            flag_lower = False
            flag_isalnum = False
            for sym in password:
                if sym.isupper():
                    flag_upper = True
                elif sym.islower():
                    flag_lower = True
                elif not sym.isalnum():
                    flag_isalnum = True
            if not flag_upper:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} символов в верхнем регистре')
            elif not flag_lower:
                raise ValueError(f'Пароль должен содержать не менее {min_lowercase} символов в нижнем регистре')
            elif not flag_isalnum:
                raise ValueError(f'Пароль должен содержать не менее {min_special_chars} спец-символов')
            return func(username, password)

        return wrapper

    return decorator


@username_validator
@password_validator()
def register_user(username: str, password: str) -> None:
    with open('users.csv', 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password])


# Тестируем
register_user('юзер1', '4erddddddddddD#$')
