import json
from dataclasses import dataclass
from typing import Set, List

from jsonschema import validate, ValidationError

"""
Экземпляр словаря для создания JSON схемы

{
        "coords": {
            "lat": "53.71667",
            "lon": "91.41667"
        },
        "district": "Сибирский",
        "name": "Абакан",
        "population": 187239,
        "subject": "Хакасия"
    }

"""

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "coords": {
            "type": "object",
            "properties": {
                "lat": {"type": "string"},
                "lon": {"type": "string"}
            },
            "required": ["lat", "lon"]
        },
        "district": {"type": "string"},
        "name": {"type": "string"},
        "population": {"type": "integer"},
        "subject": {"type": "string"}
    },
    "required": ["coords", "district", "name", "population", "subject"]
}


class Validator:
    """
    Класс для валидации данных.
    Внедряем в класс JsonFile через агрегацию (конструктор)
    Производит проверку словаря с данными на соответствие (пока просто заглушка)
    """

    def __init__(self, schema=None):
        if schema is None:
            schema = JSON_SCHEMA
        self.schema = schema

    def validate(self, data):
        """
        Метод для валидации данных
        :param data: данные для валидации
        :return: True, если данные валидны, иначе False
        """
        try:
            validate(data, self.schema)
        except ValidationError:
            return False
        return True


class JsonFile:
    """
    Класс для работы с JSON файлами.
    Методы:
    - read_data() - чтение данных из JSON файла
    - write_data() - запись данных в JSON файл
    """

    def __init__(self, file_name, validator: Validator):
        self.file_name = file_name
        self.validator = validator

    def __validate_single_city(self, city: dict) -> bool:
        """
        Метод для валидации данных о городе
        :param city: данные о городе
        :return: True, если данные валидны, иначе False
        """
        return self.validator.validate(city)

    def get_all_cities(self) -> list:
        """
        Метод который читает все города из файла и проверяет каждый город на валидность.
        Возвращает список валидных городов
        :return: список валидных городов
        """
        cities = self.__read_data()
        valid_cities = []
        for city in cities:
            if self.__validate_single_city(city):
                valid_cities.append(city)
        return valid_cities

    def __read_data(self):
        """
        Чтение данных из JSON файла
        :return: данные из JSON файла
        """
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def __write_data(self, data):
        """
        Запись данных в JSON файл
        :param data: данные для записи
        :return: None
        """
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


"""
Для следующего задания:
- Надо описать дата классы для города
- Надо внедрить это в Cities
"""


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

    # Для того, чтобы делать проверку if in
    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name
        return False


class Serializer:
    """
    Класс для десериализации данных (в будущем можно описать и сериализацию)
    Экземпляр внедряется в JsonFile через агрегацию (конструктор)
    """

    def __init__(self, city_data: list):
        self.city_data = city_data

    def __call__(self) -> List[City]:
        """
        Метод для запуска десериализации
        :return: список экземпляров класса City
        """
        return self.deserialize()

    def deserialize(self) -> List[City]:
        """
        Метод для десериализации данных
        :return: список словарей с данными о городах
        """
        cities = []
        for city in self.city_data:
            cities.append(
                City(
                    name=city['name'],
                    population=city['population'],
                    subject=city['subject'],
                    district=city['district'],
                    latitude=float(city['coords']['lat']),
                    longitude=float(city['coords']['lon'])
                )
            )
        return cities


class CityGame:
    def __init__(self, cities: List[City]):
        self.cities = cities
        self.human_city: City | None = None
        self.computer_city: City | None = None

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        """
        Метод проверки правил игры.
        Возвращает True если правила соблюдены, иначе False
        :param last_city: последний названный город
        :param new_city: новый город
        :return:
        """
        last_letter = None
        if last_city == 'Радужный':
            last_letter = 'н'
        elif last_city[-1].lower() == 'ь' or last_city[-1].lower() == 'ы' or last_city[-1].lower() == 'й':
            last_letter = last_city[-2].lower()
        else:
            last_letter = last_city[-1].lower()

        if last_letter == new_city[0].lower():
            return True
        else:
            return False

    def human_step(self):
        """
        Метод для хода человека
        :return:
        """
        self.human_city = input('Введите город: ')
        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False

        for city in self.cities:
            if city.name == self.human_city:
                if city.is_used:
                    print(f'Город {self.human_city} уже был использован. Вы проиграли')
                    return False
                else:
                    self.human_city = city
                    break
        else:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city.name, self.human_city.name):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city.name[-1]}')
                return False

        # Вместо удаления города, мы отмечаем is_used = True
        # self.cities.remove(self.human_city)

        self.human_city.is_used = True
        return True

    def computer_step(self):
        """
        Метод для хода компьютера
        :return:
        """

        for city in self.cities:
            # Проверка правил игры методом
            if self.check_game_rules(self.human_city.name, city.name):
                if city.is_used:
                    continue
                print(f'Компьютер называет город: {city.name}')
                self.computer_city = city
                city.is_used = True
                return True

        else:
            print('Вы победили! Компьютер не смог назвать город')
            return False


class GameManager:
    def __init__(self, json_file: JsonFile, game: CityGame):
        self.json_file = json_file
        self.game = game

    def __start_game(self):
        """
        Метод для начала игры
        :return:
        """
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break

    def __call__(self):
        """
        Метод для запуска игры
        :return:
        """
        self.__start_game()
        print('Игра окончена')
        input('Нажмите Enter для выхода')


if __name__ == "__main__":
    # Создаем экземпляр класса Validator
    validator = Validator()

    # Создаем экземпляр класса JsonFile
    json_file = JsonFile("./data/cities.json", validator)
    cities_data = json_file.get_all_cities()
    serializer = Serializer(cities_data)
    cities = serializer()

    game = CityGame(cities)
    game_manager = GameManager(json_file, game)
    game_manager()
