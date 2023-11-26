import json
from cities import cities_list

# cities_set = set()
# for item in cities_list:
#     cities_set.add(item['name'])
#
# with open('cities.json', 'w', encoding='utf-8') as file:
#     ensure_ascii = False
#     json.dump(list(cities_set), file, ensure_ascii=False)

with open('cities.json', 'r', encoding='UTF-8') as file:
    cities_json_string = json.load(file)
    cities_set = set(cities_json_string)

# создаём список выбывших городов, чтоб проверять, не ввёл ли юзер выбывший город. Если ввёл - он проиграл:
old_cities = []

user_input = input("Введите название города России с заглавной буквы: ")
while True:
    if user_input == 'стоп':
        print('Вы сдались! Не переживайте, получится победить в следующий раз '
              '(но навряд ли, учитывая, что я знаю все города России :-))')
        break
    if user_input in cities_set:
        old_cities.append(user_input)
    try:
        cities_set.remove(user_input)
    except KeyError:
        if user_input in old_cities:
            print('Этот город выбыл ранее. Я выиграл!')
        else:
            print('Такого города в России нет! Я выиграл!')
        break
    last_character = user_input[-1]
    # добавляем условие, обычно используемое в живой игре - если город кончается на "неподходящую" букву (й, ь, ы)
    if last_character == 'й':
        last_character = 'и'
    if last_character == 'ь' or last_character == 'ы':
        last_character = user_input[-2]
    # добавляем флаг проверки наличия в сете города для ответа юзеру (если города для ответа нет - значит, юзер выиграл)
    found_city = False
    for city in cities_set:
            cities_set.remove(city)
            # здесь не делаем проверку, как в 10 строке, т.к. компьютер абракадабру не может ввести, сразу добавляем:
            old_cities.append(city)
            last_character = city[-1]
            # здесь можно сделать функцию, чтоб не копипастить код из строк 22 - 25, но я не умею, поэтому копипаста :-)
            if last_character == 'й':
                last_character = 'и'
            if last_character == 'ь' or last_character == 'ы':
                last_character = city[-2]
            # print(last_character)
            break
    if found_city is True:
        user_input = input(f'С Вас - город на букву "{last_character.upper()}" '
                           f'или введите "стоп", если сдаётесь ')
    else:
        print('Поздравляю, Вы выиграли!')
        break
    if user_input[0] != last_character.upper() and user_input != 'стоп':
        print('Ошибка ввода. Вы проиграли!')
        break
input('Нажмите Enter для выхода')