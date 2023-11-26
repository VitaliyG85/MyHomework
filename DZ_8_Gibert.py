from marvel import full_dict

stage = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвёртая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза",

}
user_stage = input('Введите номер фазы киновселенной Marvel(цифрой): ')
result = ''
if user_stage.isalpha():
    raise TypeError('Вы ввели не число!')
elif (int(user_stage) < 1) or (int(user_stage) > 6):
    raise ValueError('Такой фазы не существует!')
if int(user_stage) in stage:
    stage_str = stage.get(int(user_stage))
    for movie in full_dict.values():
        if stage_str in (movie['stage']):
            result += movie['title'] + '\n'
print(f'В указанную Вами фазу входят следующие фильмы киновселенной Marvel:\n{result}')





