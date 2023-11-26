nums_str = input('Введите номера телефонов через точку с запятой: ')
nums_list = nums_str.split(';')
nums_list_clear = []
for num in nums_list:
    num = (num.replace('+', '').replace(' ', '').
           replace('(', '').replace(')', '').
           replace('-', ''))
    if len(num) > 11:
        raise ValueError(f'номер {num} больше 11 знаков')
    elif not (num.startswith('7') or num.startswith('8')):
        raise ValueError(f'номер {num} начинается не с +7 или 8')
    elif not num.isdigit():
        raise ValueError(f'в номере {num} есть что-то кроме чисел')
    else:
        nums_list_clear.append(num)
print(nums_list_clear)
