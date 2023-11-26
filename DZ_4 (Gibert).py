is_len = False
is_number = False
is_begin = False
res_str = ''

# input_string = input('Введите номер телефона РФ (в любом формате): ')
#
# input_string = (input_string.replace('+', '').replace(' ', '').replace('(', '')
#                 .replace(')', '').replace('-', ''))

# if len(input_string) == 11:
#     is_len = True  # Меняем флаг длины на True
# else:
#     res_str += 'Номер телефона должен состоять из 11 символов\n'
#
# if input_string.startswith('7') or input_string.startswith('8'):
#     is_begin = True  # Меняем флаг начала номера на True
# else:
#     res_str += 'Номер телефона РФ должен начинаться на +7 или 8\n'
#
# if input_string.isdigit():
#     is_number = True  # Меняем флаг проверки на числа на True
# else:
#     res_str += 'Номер телефона должен состоять только из цифр\n'
#
# if is_len and is_begin and is_number:
#     res_str = 'Номер телефона введён верно'
# else:
#     res_str += 'Номер телефона введён неверно'
# print(res_str)

input_password = input('Придумайте и введите пароль:')
if ((len(input_password) > 7)
        and (not (input_password.isalnum() or input_password.islower() or input_password.isupper()))
        and input_password.find(' ') == -1):
    print('Пароль принят')
else:
    print('Пароль недостаточно надежный или содержит пробел(ы)')
