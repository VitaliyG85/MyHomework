from abc import ABC, abstractmethod
from typing import Dict


class SmartDevice(ABC):
    """
    Абстрактный класс для умных устройств.
    """

    def __init__(self, name: str):
        """
        Инициализация умного устройства.

        :param name: название устройства
        """
        self.name = name

    def __str__(self):
        return f'{self.name}'

    @abstractmethod
    def turn_on(self):
        """ Включить устройство. """
        pass

    @abstractmethod
    def turn_off(self):
        """ Выключить устройство. """
        pass

    @abstractmethod
    def get_state(self):
        """ Получить текущее состояние устройства. """
        pass


class SmartBulb(SmartDevice):
    """
    Класс для умной лампочки.
    """

    def __init__(self, name: str):
        """
        Инициализация умной лампочки.

        :param name: название лампочки
        """
        super().__init__(name)
        self.state = False
        self.brightness = 0

    def turn_on(self):
        """
        Включить лампочку.
        :return: None
        """
        self.state = True

    def turn_off(self):
        self.state = False

    def get_state(self):
        """
        Получить текущее состояние лампочки.
        :return: строка с состоянием лампочки
        """
        return f"Лампочка {'включена' if self.state else 'выключена'}, яркость: {self.brightness}"

    def set_brightness(self, brightness: int):
        """
        Регулировать яркость лампочки.

        :param brightness: уровень яркости
        """
        self.brightness = brightness


class SmartSmokeDetector(SmartDevice):
    """
    Класс для умного датчика дыма.
    """

    def __init__(self, name: str):
        """
        Инициализация умного датчика дыма.

        :param name: название датчика
        """
        super().__init__(name)
        self.state = False
        self.smoke = False

    def turn_on(self):
        """
        Включить датчик дыма.

        """
        self.state = True

    def turn_off(self):
        """
        Выключить датчик дыма.
        """
        self.state = False

    def get_state(self):
        """
        Получить текущее состояние датчика дыма.
        :return: строка с состоянием датчика дыма
        """
        return f"Датчик дыма {'включен' if self.state else 'выключен'}"

    def check_smoke(self):
        """
        Проверить наличие дыма.

        :return: True если дым обнаружен, иначе False
        """

        return False


class SmartHumidifier(SmartDevice):
    """
    Класс для умного увлажнителя воздуха.
    """

    def __init__(self, name: str):
        """
        Инициализация умного увлажнителя воздуха.

        :param name: название увлажнителя
        """
        super().__init__(name)
        self.state = False
        self.humidity_level = 0

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def get_state(self):
        return f"Увлажнитель {'включен' if self.state else 'выключен'}, уровень влажности: {self.humidity_level}"

    def set_humidity(self, humidity_level: int):
        """
        Установить уровень влажности.

        :param humidity_level: уровень влажности
        """
        self.humidity_level = humidity_level


class UrgentNotificationMixin:
    """
    Миксин для срочного уведомления.
    """

    def send_urgent_notification(self, message: str):
        """
        Отправить срочное уведомление.

        :param message: сообщение уведомления
        """
        print(f"Срочное уведомление: {message}")


class WiFiConnectionMixin:
    """
    Миксин для подключения к Wi-Fi.
    """

    def connect_to_wifi(self, network_name: str, password: str):
        """
        Подключиться к Wi-Fi сети.

        :param network_name: имя Wi-Fi сети
        :param password: пароль Wi-Fi сети
        """
        # Здесь может быть логика подключения к Wi-Fi
        print(f"Устройство {self} подключено к Wi-Fi сети {network_name}")


class ScheduleMixin:
    """
    Миксин для работы по расписанию.
    """

    def __init__(self):
        self.schedule = {}

    def set_schedule(self, schedule: Dict[str, str]):
        """
        Задать расписание работы устройства.

        :param schedule: расписание в формате {время: действие}
        """
        self.schedule = schedule


class SmartBulbPhilips(SmartBulb, WiFiConnectionMixin):
    """
    Умная лампочка Philips.
    """

    def __str__(self):
        return f'Умная лампочка Philips'


class SmartSmokeDetectorXiaomi(SmartSmokeDetector, WiFiConnectionMixin, UrgentNotificationMixin):
    """
    Умный датчик дыма Xiaomi.
    """

    def __str__(self):
        return f'Умный датчик дыма Xiaomi'


class SmartHumidifierBosch(SmartHumidifier, WiFiConnectionMixin, ScheduleMixin):
    """
    Умный увлажнитель Bosch.
    """

    def __str__(self):
        return f'Умный увлажнитель Bosch'


# Симуляция работы умного дома
bulb = SmartBulbPhilips("Гостиная")
bulb.connect_to_wifi("Домашний Wi-Fi", "пароль123")
smoke_detector = SmartSmokeDetectorXiaomi("Кухня")
humidifier = SmartHumidifierBosch("Спальня")
humidifier.set_schedule({"08:00": "включить", "23:00": "выключить"})

bulb.turn_on()  # Включить лампочку
bulb.set_brightness(70)  # Установить яркость 70%
smoke_detector.turn_on()  # Включить датчик дыма
humidifier.turn_on()  # Включить увлажнитель
humidifier.set_humidity(50)  # Установить уровень влажности 50%
humidifier.connect_to_wifi("Домашний Wi-Fi", "пароль123")

print(bulb.get_state())  # Получить состояние лампочки
print(smoke_detector.get_state())  # Получить состояние датчика дыма
print(humidifier.get_state())  # Получить состояние увлажнителя

if smoke_detector.check_smoke():  # Проверить наличие дыма
    smoke_detector.send_urgent_notification("Обнаружен дым на кухне!")  # Отправить срочное уведомление

