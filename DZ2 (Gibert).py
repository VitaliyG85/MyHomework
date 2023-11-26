all_time = int(input('Введите количество секунд: '))
hours = all_time // 3600
minutes = (all_time % 3600) // 60
seconds = all_time % 60
print(f'В указанном количестве секунд ({all_time}):\nЧасов:{hours}\nМинут:{minutes}\nСекунд {seconds}')

celsius = float(input("Введите температуру в градусах Цельсия: "))
kelvin = round(celsius + 273.15, 2)
fahrenheit = round(celsius * 1.8 + 32, 2)
reomur = round(celsius * 0.8, 2)
print(f'В указанном количестве градусов цельсия:{celsius}'
      f'\nГрадусов Кельвина: {kelvin}'
      f'\nГрадусов Фаренгейта: {fahrenheit}'
      f'\nГрадусов Реомюра: {reomur}')