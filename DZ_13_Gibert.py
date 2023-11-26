from marvel import full_dict
from typing import List, Optional, Dict, Union
from pprint import pprint

user_list: List[str] = input('Введите порядковые номера фильмов Марвел: ').split()
nums_list: List[Optional[int]] = list(
    map(lambda str_num: int(str_num) if str_num.isdigit() else None, user_list))

# Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id и
# остальные ключи, но только тех фильмов, id которых есть в полученном списке в п.2

filtered_full_dict_by_ID: Dict[int, Dict] = dict(filter(lambda movie: movie[0] in nums_list, full_dict.items()))

# Составьте set comprehension (генератор множества) собрав множество содержимого ключа director
# словаря дата-сета

directors_set: set = {value['director'] for value in filtered_full_dict_by_ID.values() if value['director'] != 'TBA'}

# Составьте dict comprehension (генератор словаря) сделав копию исходного словаря full_dict , при этом
# применим к каждому 'year' значению, функцию str

full_dict_year_str: Dict[int, Dict[str, str]] = {key:
                                                     {'title': value['title'],
                                                      'year': str(value['year']),
                                                      'director': value['director'],
                                                      'screenwriter': value['screenwriter'],
                                                      'producer': value['producer'],
                                                      'stage': value['stage']}
                                                 for key, value in full_dict.items()}

# Сделайте сортировку словаря full_dict по одному (любому) параметру, с использованием lambda на выходе
# аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете сортировку!

filtered_full_dict_by_Ch: Dict[int, Dict] = dict(
    filter(lambda movie: movie[1]['title'].startswith('Ч'), full_dict.items()))

# Сделайте сортировку словаря full_dict по одному (любому) параметру, с использованием lambda на выходе
# аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете сортировку!

# делаем сортировку фильмов, которые продюссировал Кевин Файги (всё-таки глава Marvel Studios :)
filtered_full_dict_by_Kevin: Dict[int, Dict] = dict(filter(lambda movie: 'Кевин Файги' in movie[1]['producer'],
                                                           full_dict.items()))

# Опционально: сделайте сортировку словаря full_dict по двум (любом) параметрам, с использованием lambda
# на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете
# сортировку!

# делаем сортировку фильмов, которые продюссировал Кевин Файги, а снимал Джон Фавро (так как ЖЧ-1 - the Best))

filtered_full_dict_by_Kevin_and_John: Dict[int, Dict] = dict(filter(lambda movie: 'Кевин Файги' in movie[1]['producer']
                                                                                  and 'Джон Фавро' in movie[1][
                                                                                      'director'],
                                                                    full_dict.items()))

# Сделайте красивый принт результатов pprint с подписью, какое задание и где выполнено 💪 (помните, что
# у него надо выключить сортировку, иначе он сортирует словарь еще раз)

print(' ')
print('Словарь фильмов, выбранных пользователем:\n')
pprint(filtered_full_dict_by_ID, sort_dicts=False)
print(' ')
print('Сет режиссёров фильмов, выбранных пользователем:\n')
pprint(directors_set, sort_dicts=False)
print(' ')
print('Словарь фильмов, в котором параметр "year" приведён к str:\n')
pprint(full_dict_year_str, sort_dicts=False)
print(' ')
print('Словарь фильмов, которые начинаются на букву "Ч":\n')
pprint(filtered_full_dict_by_Ch, sort_dicts=False)
print(' ')
print('Словарь фильмов, в которых хотя бы одним из продюсеров был Кевин Файги:\n')
pprint(filtered_full_dict_by_Kevin, sort_dicts=False)
print(' ')
print('Словарь фильмов, в которых хотя бы одним из продюсеров был Кевин Файги, а режиссёром - Джон Фавро:\n')
pprint(filtered_full_dict_by_Kevin_and_John, sort_dicts=False)
