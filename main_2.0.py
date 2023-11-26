import json
# from cities import cities_list


# cities_set = set()
# for item in cities_list:
#     cities_set.add(item['name'])
#
# with open('cities.json', 'w', encoding='utf-8') as file:
#     ensure_ascii = False
#     json.dump(list(cities_set), file, ensure_ascii=False)

# with open('cities.json', 'r', encoding='UTF-8') as file:
#     cities_json_string = json.load(file)
#     cities_set = set(cities_json_string)


def get_cities_set_from_json(file_name: str = 'cities.json') -> set:
    """
    Чтение файла json с городами и возвращение сета городов
    :param file_name: По умолчанию 'cities.json'
    :return:Сет городов
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        cities_json_string = json.load(file)
        cities_set = set(cities_json_string)
    return cities_set


def check_main_game_rule(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и, во-первых, проверяет, не заканчивается ли город last_round_city на "плохую букву",
    если заканчивается - меняет на "хорошую" ("Й" меняет на "И", "Ь" или "Ы" меняет на предпоследнюю букву города),
    во-вторых, проверяет, что первая буква города current_round_city
    равна последней букве города last_round_city
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    last_ch = last_round_city[-1]
    if last_ch == 'й':
        last_ch = 'и'
    if last_ch == 'ь' or last_ch == 'ы':
        last_ch = last_round_city[-2]
    if last_ch == current_round_city[0].lower():
        return True
    else:
        return False


def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает сет городов, город из прошлого раунда. Проходит циклом по сету
    городов, проверяя каждый город на главное правило игры
    :param cities_set:
    :param last_round_city:
    :return:
    """
    for city in cities_set:
        if check_main_game_rule(last_round_city, city):
            return city
    else:
        return None


def main():
    # Создаём список выбывших городов, чтоб проверять, не ввёл ли юзер выбывший город. Если ввёл - он проиграл:
    old_cities = []
    # объявляем переменную под ход компьютера
    computer_input = None
    while cities_set:
        # Пользовательский ввод данных - излишне делать по нему функцию:
        user_input = input("Введите город РФ с заглавной буквы: ")

        # Проверка на стоп
        if user_input == 'стоп':
            print('Вы сдались! Не переживайте, получится победить в следующий раз '
                  '(но навряд ли, учитывая, что я знаю все города России :-))')
            break

        # Проверка на наличие города в сете выбывших городов
        if user_input in old_cities:
            print('Этот город выбыл ранее. Я выиграл!')
            break

        # Проверка на наличие города в сете существующих городов РФ
        if user_input not in cities_set:
            print('Такого города в России нет или у вас опечатка. Я выиграл!')
            break

        # проверка на совпадение последней буквы
        if computer_input:
            if not check_main_game_rule(computer_input, user_input):
                print('Вы назвали город не на ту букву! Вы проиграли!')
                break

        # убираем выбывший город из сета городов
        cities_set.remove(user_input)

        # добавляем выбывший город в сет выбывших городов
        old_cities.append(user_input)

        # Принт ход человека
        print(f'Вы ввели: {user_input}')

        # ход компьютера

        computer_input = computer_move(cities_set, user_input)

        if not computer_input:
            print('Вы выиграли')
            # Логирование
            break
        # убираем выбывший город из сета городов
        cities_set.remove(computer_input)
        # добавляем выбывший город в сет выбывших городов
        old_cities.append(computer_input)

        # Печатаем ход компьютера
        print(f'Мой город: {computer_input}.')
    else:
        print('Вы терминатор. Вы выиграли!')
        # Логирование


cities_set = get_cities_set_from_json()
main()
input('Нажмите Enter для выхода')
